from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RequestBody(BaseModel):
    question: str

@app.post("/ask")
def ask_model(data: RequestBody):
    return {"answer": f"Received your question: {data.question}"}