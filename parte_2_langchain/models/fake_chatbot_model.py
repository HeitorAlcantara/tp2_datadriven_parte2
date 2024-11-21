from pydantic import BaseModel

class FakeChatBot(BaseModel):
    fake_response: str