# Get Website Content

import requests

def Send(Url:str) -> str:
    rep_content = requests.get(url=Url)
    return rep_content.text