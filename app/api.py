from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Fintech Portfolio API", version="1.0.0")

class Client(BaseModel):
    name: str = Field(min_length=2)
    risk_level: str = Field(pattern="^(Low|Medium|High)$")
    balance: float = Field(ge=0)

clients = {
    1: {"id": 1, "name": "Aarav Mehta", "risk_level": "Low", "balance": 125000.0},
    2: {"id": 2, "name": "Maya Shah", "risk_level": "Medium", "balance": 78000.0},
}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/clients")
def get_clients():
    return list(clients.values())

@app.get("/clients/{client_id}")
def get_client(client_id: int):
    if client_id not in clients:
        raise HTTPException(status_code=404, detail="Client not found")
    return clients[client_id]

@app.post("/clients", status_code=201)
def create_client(client: Client):
    new_id = max(clients) + 1 if clients else 1
    record = {"id": new_id, **client.model_dump()}
    clients[new_id] = record
    return record
