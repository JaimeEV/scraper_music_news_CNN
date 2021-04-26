import requests 
import lxml.html as html
import os
import datetime

#CNN Music
LINK_CNN_MUSIC = 'https://cnnespanol.cnn.com/category/musica/'
XPATH_LINK_TO_ARTICLE = '//h2[@class="news__title"]/a/@href'
XPATH_TITLE = '//div[@class="news__data"]/h1[@class="news__title"]/text()'
XPATH_CONTAIN = '//div[@class="news__excerpt"]/p/text()'




def parse_notices(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                title = title.replace('\"','').strip()
                contain = parsed.xpath(XPATH_CONTAIN)[0]
            except IndexError: 
                return
            
            with open(f'{today}/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(contain)
        else:
            raise ValueError(f'Error: {respones.status_code}')
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(LINK_CNN_MUSIC)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            # print(links_to_notices)

            today = datetime.date.today().strftime('%d-%m-%Y')
            if not os.path.isdir(today):
                os.mkdir(today)

            for link in links_to_notices:
                parse_notices(link, today)
        else:
            raise ValueError(f'Error: {status_code}')
    except ValueError as ve:
        print(ve)


def run():
    parse_home()


if __name__ == '__main__':
    run()