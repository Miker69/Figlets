import requests
import urllib3
import scripts.decorate as decor


def parse_font19():
    try:
        url = 'https://www.topster.su/text-to-ascii/relief.html'
        text = input('Enter text: ')

        x = {'text': text}
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        page = requests.post(url, data=x, verify=False)
        decor.request_info(page, url)
    except Exception as e:
        print(e)
