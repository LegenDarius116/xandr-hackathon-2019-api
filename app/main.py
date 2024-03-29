import json
from fastapi import FastAPI
from chatbot import MastodonBot
from dotenv import load_dotenv
from model.predict import PredictionModel

load_dotenv()

app = FastAPI()
bot = MastodonBot()
predictionModel = PredictionModel()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/analyze/{test}")
def analyze(test: str):
    prediction = predictionModel.predict(test)
    return {"input": test,
            "prediction": prediction,
            "filter": True if prediction > 0.5 else False}


@app.get("/report/{user}/{status_id}")
def report(user: str, status_id: int):
    return bot.reply_to(user, status_id)

