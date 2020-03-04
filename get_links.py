import requests
from bs4 import BeautifulSoup
import sys, os
import subprocess


def get_links(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')
    return [v['href'] for v in soup.find_all('a', href=True) if v['href'].startswith('http')]


def main():
    num_processes = int(sys.argv[1])
    url = sys.argv[2]

    links = get_links(url)
    print(len(links), url)

    urls_per_process = len(links) // num_processes
    start, end = 0, urls_per_process + len(links) % num_processes  # увеличиваем на величину остатка

    subps = []

    while start < len(links):
        print(f'spawning subprocess with {len(links[start:end])} links')
        cmd = [sys.executable, 'get_links_child.py', *links[start:end]]
        sp = subprocess.Popen(cmd)
        subps.append(sp)
        print(f'Started subprocess {sp.pid}')
        start, end = end, end + urls_per_process

    while subps:
        sp = subps.pop()
        sp.wait()
        # for line in sp.stdout:
        #     print(line)
        print(f'Subprocess {sp.pid} done')


if __name__ == '__main__':
    main()
