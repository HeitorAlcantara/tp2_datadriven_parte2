from fastapi import FastAPI
from models.fake_chatbot_model import FakeChatBot
from models.gemini_model import GeminiModel
from models.huggingface_translator_model import TranslateModel
from langchain_community.llms import FakeListLLM
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from transformers import pipeline


app = FastAPI()

@app.post("/fakellm")
async def fakechatbot(response: FakeChatBot) -> str:
    fake_llm = FakeListLLM(responses = ["Hi, i'm fake chatbot. What's your name?",
                                        "I like to read and play videogames!",
                                        "Boa noite!",
                                        "Desktop needs electricity to work."])

    return fake_llm.invoke(response.fake_response)



@app.post("/gemini")
async def gemini_en_fr(text: GeminiModel) -> dict:
    template = ChatPromptTemplate([
        ("system", "You are a helpful assistant that only translates English to French. Translate the user sentence."),
        ("user", "Translate this {text}")
    ])
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
    response = llm.invoke(template.format(text=text))
    return {"user": text.text, "gemini": response.content}


def generate_response(message: str):
    generator = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")
    return generator(message)


@app.post("/translate")
async def translate(body: TranslateModel):
    response = generate_response(body.en_phrase)
    return {"user": body.en_phrase, "assistant": response[0]['translation_text']}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)