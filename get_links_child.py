from get_links import get_links
import sys
import os


def main():
    urls = sys.argv[1:]
    for url in urls:
        links = get_links(url)
        print(os.getpid(), len(links), url)


if __name__ == '__main__':
    main()
