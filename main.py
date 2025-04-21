import asyncio

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

async def fake_stream():
    words = ["Hello", "there,", "this", "is", "a", "streamed", "message."]
    for word in words:
        yield word + " "
        await asyncio.sleep(0.3)

@app.get("/message")
async def message():
    return StreamingResponse(
        fake_stream(),
        media_type="text/plain"
    )