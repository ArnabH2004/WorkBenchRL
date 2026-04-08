from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

current_step = 0

class StepRequest(BaseModel):
    action: str

@app.post("/reset")
def reset():
    global current_step
    current_step = 0
    return {
        "observation": "Task started",
        "done": False
    }

@app.post("/step")
def step(request: StepRequest):
    global current_step
    current_step += 1

    reward = 0.10
    done = current_step >= 3

    return {
        "observation": f"Processed: {request.action}",
        "reward": round(reward, 2),
        "done": done,
        "info": {}
    }

def main():
    return app