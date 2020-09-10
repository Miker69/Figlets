import requests
import urllib3
import scripts.decorate as decor


def parse_font14():
    try:
        url = 'https://www.topster.su/text-to-ascii/banner3.html'
        text = input('Enter text: ')

        x = {'text': text}
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        page = requests.post(url, data=x, verify=False)
        decor.request_info(page, url)
    except Exception as e:
        print(e)
