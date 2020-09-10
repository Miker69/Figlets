import requests
from bs4 import BeautifulSoup
import urllib3


def request_info(html, i):
    soup = BeautifulSoup(html.text, 'lxml')
    line = soup.find('main').find('pre')

    colors = {1: '\033[31m', 2: '\033[32m', 3: '\033[33m', 4: '\033[34m',
              5: '\033[35m', 6: '\033[36m', 7: '\033[93m', 8: '\033[94m',
              9: '\033[95m', 10: '\033[96m', 11: '\033[0m'}

    print('Color text?')

    question = input('Enter your answer(Enter Y or N): ')
    print(f"""
    1. red
    2. green
    3. orange
    4. blue
    5. purple
    6. cyan
    7. yellow
    8. lightblue
    9. pink
    10.ligth cyan 
    """)

    if question.upper() == 'Y':

        color = int(input('Color: '))

        try:
            if 0 < color < 11:
                with open('all_design.txt', 'a') as file:
                    file.write(
                        f"{chr(10)}{'-' * 35}{chr(10) + i.replace('.html', '').upper() + chr(10)}{'-' * 35} {chr(10)}")
                    file.write(
                        f"print(\\033{colors.get(color)} +{chr(10) + line.text + chr(10)}  + \\033{colors.get(color) + chr(10)})")

            else:
                print('Enter right color!')
        except Exception as e:
            print(e)
    elif question.upper() == 'N':
        with open('all_design.txt', 'a') as file:
            file.write(
                f"{chr(10)}{'-' * 35}{chr(10) + i.replace('.html', '').upper() + chr(10)}{'-' * 35} {chr(10)}")
            file.write(f"print({chr(10) + line.text + chr(10)} )")
    else:
        print('Enter Y or N!')


def parse_font1():
    try:
        urls = ['bubble.html', 'starwars.html', 'alpha.html', 'fender.html', 'doom.html', 'gothic.html',
                'graffiti.html',
                'rammstein.html', 'avatar.html', 'sub-zero.html', 'binary.html', 'epic.html', 'jacky.html',
                'runyc.html',
                'shadow.html', 'slant.html', 'heart_right.html', 'twisted.html', 'relief.html',
                'linux.html']
        text = input('Enter text: ')
        for i in urls:
            url = 'https://www.topster.su/text-to-ascii/' + i

            x = {'text': text}
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            page = requests.post(url, data=x, verify=False)
            request_info(page, i)

    except Exception as e:
        print(e)
    finally:
        print('Done!')
