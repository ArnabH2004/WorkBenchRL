import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

# ==============================
# ENV VARIABLES (REQUIRED)
# ==============================

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

# OpenAI client (REQUIRED by guidelines)
client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

# ==============================
# FASTAPI APP
# ==============================

app = FastAPI()

# ==============================
# STATE (simple demo state)
# ==============================

current_step = 0

# ==============================
# REQUEST FORMAT
# ==============================

class StepRequest(BaseModel):
    action: str

# ==============================
# RESET ENDPOINT (MANDATORY)
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
# STEP ENDPOINT (MANDATORY)
# ==============================

@app.post("/step")
def step(request: StepRequest):
    global current_step
    current_step += 1

    action = request.action

    # Simple deterministic logic (baseline agent)
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
# ROOT ENDPOINT (OPTIONAL)
# ==============================

@app.get("/")
def root():
    return {"status": "WorkBenchRL is running 🚀"}
