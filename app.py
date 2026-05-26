from fastapi import FastAPI
from agent import Agent03
app = FastAPI(title="Enterprise-Policy-Guardian")
agent = Agent03()

@app.post("/execute")
async def execute(payload: dict):
    return agent.execute(payload)
