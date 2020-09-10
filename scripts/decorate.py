from bs4 import BeautifulSoup
import sys

menu = (f"""
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


def request_info(html, url):
    soup = BeautifulSoup(html.text, 'lxml')
    line = soup.find('main').find('pre')
    print('Color text?')
    question = input('Enter your answer(Enter Y or N): ')

    colors = {1: '\033[31m', 2: '\033[32m', 3: '\033[33m', 4: '\033[34m',
              5: '\033[35m', 6: '\033[36m', 7: '\033[93m', 8: '\033[94m',
              9: '\033[95m', 10: '\033[96m', 11: '\033[0m'}
    if question.upper() == 'Y':

        print(menu)
        color = int(input('Color: '))

        try:
            if 0 < color < 11:
                print(colors[color] + line.text + colors[11])
            else:
                print('Enter right color!')

            answer = input('Save text to a file?(Y/N)')
            if answer.upper() == 'Y':

                url = url.replace('https://www.topster.su/text-to-ascii/', '')
                with open(url.replace('.html', '') + '.txt', 'w') as file:
                    file.write(
                       f"print('\\033{str(colors.get(color)).replace(' ', '')}' + r'''{chr(10) + line.text + chr(10)}'''  + '\\033{str(colors.get(color)).replace(' ', '')}')")

            elif answer.upper() == 'N':
                print(line.text)
                sys.exit()
            else:
                print('Enter Y/N!')

        except Exception as e:
            print(e)

    elif question.upper() == 'N':
        print(line.text)
    else:
        print('Enter Y or N!')
