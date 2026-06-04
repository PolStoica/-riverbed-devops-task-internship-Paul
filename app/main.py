"""Simple FastAPI app with a Redis-backed visit counter."""

import os

import redis
import random
import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

app = FastAPI(title="DevOps Intern Demo", version="0.1.0")
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


### Bakend API endpoints
@app.get("/health")
def health() -> dict:
    try:
        r.ping()
        redis_ok = True
    except redis.RedisError:
        redis_ok = False
    return {"status": "ok", "redis": redis_ok}

@app.get("/visits")
def visits() -> dict:
    count = r.incr("visits")
    return {"visits": count}

@app.get("/visits/count")
def visits_count() -> dict:
    count = r.get("visits")
    return {"visits": int(count) if count else 0}

@app.post("/visits/reset")
def visits_reset() -> dict:
    r.set("visits", 0)
    return {"visits": 0}

# Minimal UI
@app.get("/index", response_class=HTMLResponse)
def index() -> str:
    count = visits()["visits"]
    visits_count = int(count) if count else 0
    visits_text = "no" if visits_count == 0 else visits_count
    text = f"""
        <h1>Hello, you visited this page {visits_text} times</h1>
        <button onclick="fetch('/visits/reset', {{method:'POST'}}).then(() => location.reload())">
            Reset
        </button>
        """
    return text