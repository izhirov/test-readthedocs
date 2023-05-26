import requests


def fetch_yandex_main_page(headers: dict):
    """Fetch yandex main page.

    Arguments:
        headers {dict} -- Extra headers

    Return
        response {Response} -- Response
    """
    headers = headers or {}
    url = 'https://yandex.ru'
    response = requests.get(url, headers=headers)
    return response.json()


def fetch_google_main_page(headers: dict):
    """Fetch google main page.

    Arguments:
        headers {dict} -- Extra headers

    Return
        response {Response} -- Response
    """
    headers = headers or {}
    url = 'https://google.com'
    response = requests.get(url, headers=headers)
    return response.json()
