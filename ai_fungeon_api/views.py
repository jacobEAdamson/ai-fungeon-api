from flask import request
import requests
import json

from ai_fungeon_api import app
from ai_fungeon_api.services.ai_chat_service import AiChatService

@app.route('/')
def index():
    person_name = request.args.get('person_name')
    user_ip = request.remote_addr
    if user_ip == "127.0.0.1":
        user_ip = json.loads(requests.get("https://api.ipify.org?format=json").text)["ip"]

    url = f'https://apip.cc/api-json/{user_ip}'
    response = requests.get(url)
    data = json.loads(response.text)
    location = f'{data["City"]}, {data["RegionName"]}'

    ai_chat_service = AiChatService()
    return ai_chat_service.write_story(location, person_name)
