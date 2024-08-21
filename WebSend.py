# Get Website Content

import requests


def Send(Url: str, Method: str = 'GET', **kwargs) -> str:
    if Method == 'GET':
        rep_content = requests.get(url=Url)
        return rep_content.text
    if Method == 'POST':
        header = {} if 'header' not in kwargs else kwargs['header']
        data = kwargs['data']
        rep_content = requests.post(url=Url, headers=header, data=data)
