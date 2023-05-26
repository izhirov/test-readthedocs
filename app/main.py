from app.api import fetch_yandex_main_page, fetch_google_main_page


if __name__ == '__main__':
    # This is a comment about the code below
    fetch_yandex_main_page(headers={})
    fetch_google_main_page(headers={'foo': 'bar'})
