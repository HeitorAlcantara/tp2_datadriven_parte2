from pydantic import BaseModel

class TranslateModel(BaseModel):
    en_phrase: str