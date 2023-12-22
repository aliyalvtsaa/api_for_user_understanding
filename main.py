from fastapi import FastAPI
from understanding_user.langchain_understand_user import AI_understanding
from pydantic import BaseModel
from contextlib import asynccontextmanager

class UserRequest(BaseModel):
    text: str

app = FastAPI()
ai = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global ai
    ai = AI_understanding()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/process")
async def process_request(request: UserRequest):
    response = await ai.ask_ai(request.text)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
