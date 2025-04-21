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
    import random
    words = [
        "Hello", "there,", "this", "is", "a", "streamed", "message.",
        "It", "is", "being", "sent", "word", "by", "word.",
        "You", "can", "see", "how", "it", "works", "in", "real-time.",
        "This", "is", "a", "simple", "example", "of", "streaming", "data.",
        "FastAPI", "makes", "it", "easy", "to", "create", "APIs", "like", "this.",
        "You", "can", "use", "it", "for", "various", "applications,", "like",
        "real-time", "notifications,", "chat", "applications,", "or", "live", "updates.",
    ]

    for word in words:
        yield word + " "
        await asyncio.sleep(random.uniform(0.01, 0.5)) 

@app.get("/message")
async def message():
    return StreamingResponse(
        fake_stream(),
        media_type="text/plain"
    )