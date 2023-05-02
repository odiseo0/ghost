from langchain.llms import OpenAI
from fastapi import FastAPI


app = FastAPI()
llm = OpenAI(temperature=0.9, max_tokens=-1)


@app.get("/")
async def index(q: str):
    return llm(q)
