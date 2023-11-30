import requests


class TelegramAPI:
    request_str = 'https://api.telegram.org/bot'

    @staticmethod
    def request(token: str, method: str, request_timeout, **kwargs) -> requests.Response:
        url: str = f'{TelegramAPI.request_str}{token}/{method}'
        return requests.get(url, params=kwargs, timeout=request_timeout)
