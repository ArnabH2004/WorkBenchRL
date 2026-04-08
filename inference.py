import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

# ==============================
# ENV VARIABLES (SAFE VERSION)
# ==============================

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
HF_TOKEN = os.getenv("HF_TOKEN")

# ✅ FIX: Do NOT crash if missing
if HF_TOKEN is None:
    print("⚠️ Warning: HF_TOKEN not set. Running in fallback mode.")

# OpenAI client (only if token exists)
client = None
if HF_TOKEN:
    client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

# ==============================
# FASTAPI APP
# ==============================

app = FastAPI()

# ==============================
# STATE
# ==============================

current_step = 0

# ==============================
# REQUEST MODEL
# ==============================

class StepRequest(BaseModel):
    action: str

# ==============================
# RESET ENDPOINT (REQUIRED)
# ==============================

@app.post("/reset")
def reset():
    global current_step
    current_step = 0

    return {
        "observation": "Task started",
        "done": False
    }

# ==============================
# STEP ENDPOINT (REQUIRED)
# ==============================

@app.post("/step")
def step(request: StepRequest):
    global current_step
    current_step += 1

    action = request.action

    # Deterministic logic (baseline)
    reward = 0.10
    done = False

    if current_step >= 3:
        done = True

    return {
        "observation": f"Processed action: {action}",
        "reward": round(reward, 2),
        "done": done,
        "info": {}
    }

# ==============================
# HEALTH CHECK
# ==============================

@app.get("/")
def root():
    return {"status": "WorkBenchRL is running 🚀"}
