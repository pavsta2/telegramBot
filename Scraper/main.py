import re
import random
from typing import Union

from bs4 import BeautifulSoup
import requests


class Parser:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.0.1841 Yowser/2.5 Safari/537.36',
            'Accept-Language': 'ru',
        }

    def get_pages_links(self) -> Union[None, dict]:
        """метод возвращает словарь со ссылками на все страницы сайта"""
        links_dict = {"https://www.hirobots.spb.ru": False}
        links_queue = {"https://www.hirobots.spb.ru"}

        def recursion_func(link: str):
            if all(links_dict.values()):
                return None
            links_dict[link] = True
            request = self.session.get(link)
            bs = BeautifulSoup(request.text, 'html.parser')
            all_links = bs.find_all('a')
            for l in all_links:
                print(l)
                try:
                    if 'https://www.hirobots.spb.ru' in l['href'] and l['href'] not in links_dict.keys() \
                            and request.status_code == 200:
                        links_queue.add(l['href'])
                        print(l['href'])
                        links_dict[l['href']] = False
                except:
                    continue
            try:
                link = links_queue.pop()
            except:
                link = None
            recursion_func(link)
            return links_dict

        return recursion_func(links_queue.pop())

    def get_images(self, link: str) -> set:
        """Метод возвращает множество со ссылками на все фотографии с сайта """
        request = self.session.get(link)
        image_url_begin = 'https://static.wixstatic.com/media/'
        bs = BeautifulSoup(request.text, 'html.parser')
        all_links = bs.find_all('wix-image', class_='_1-6YJ _2r0F8')

        links_set = set()
        for link in all_links:
            photo_link = image_url_begin + re.compile('b7\S+.jpg').search(
                link['data-image-info']).group()
            links_set.add(photo_link)
        return links_set

    @staticmethod
    def image_download(self, links_set):
        """метод сохраняет фото в текущую папку"""
        for link in links_set:
            photo = requests.get(link)
            with open(f'{random.choice(range(0, 10000))}.jpg', 'wb') as f:
                f.write(photo.content)
                print(f'загружено фото {f.name}.jpg')


def main():
    parser = Parser()
    pages = parser.get_pages_links()
    print(pages)
    total_link_set = set()
    for page in pages.keys():
        images = parser.get_images(page)
        total_link_set = total_link_set.union(images)

    print(total_link_set)
    print(len(total_link_set))

    parser.image_download(total_link_set)


if __name__ == '__main__':
    main()
