import uvicorn
from fastapi import FastAPI
from pprint import pprint
import httpx
from pydantic import BaseModel
from environs import Env


env = Env()
env.read_env()

app = FastAPI()


url = env("API_URL", "https://api.pachca.com/api/shared/v1/messages")
auth_token = env("AUTH_TOKEN")

message_data = {
    "message": {
        "entity_type": "discussion",
        "entity_di": 15727441,
        "content": "Привет, это тестовое сообщение!",
        "files": [],
        "buttons": [
            [
                {
                    "text": "Опция 1",  
                    "data": "option_1"  
                },
                {
                    "text": "Опция 2",  
                    "data": "option_2"  
                },
            ]
        ],
        "parent_message_id": None,
        "skip_invite_mentions": False,
        "link_preview": True
    }
}

headers = {
    "Authorization": f"Bearer {auth_token}",
    "Content-Type": "application/json; charset=utf-8"
}


@app.post("/send_message")
async def send_message():
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=message_data, headers=headers)

    if response.status_code == 200:
        print("Сообщение успешно отправлено!")
        pprint(response.json())
        return {"status": "success", "data": response.json()}
    else:
        pprint(f"Ошибка при отправке сообщения: {response.status_code}")
        pprint(response.json())
        return {"status": "error", "data": response.json()}, response.status_code


class ButtonEvent(BaseModel):
    type: str | None = None
    message_id: int | None = None
    data: str | None = "vote_yes"
    user_id: int | None = 18531312 


@app.post("/webhook")
async def webhook(event: ButtonEvent):
    print("Received webhook data:")
    pprint(event)
    
    return {"status": "success"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)