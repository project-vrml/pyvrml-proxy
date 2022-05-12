import requests as requests

_url = "http://www.baidu.com"


def bark():
    response = requests.get(url=_url)

    print(response.text)


if __name__ == '__main__':
    bark()
