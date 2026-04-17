from fastapi import FastAPI
from agent import build_graph
from models import Base
from database import engine

app = FastAPI()
graph = build_graph()

Base.metadata.create_all(bind=engine)

@app.post("/chat")
def chat(input: dict):
    result = graph.invoke({"input": input["message"]})
    return result

@app.get("/interactions")
def get_data():
    from database import SessionLocal
    from models import Interaction
    db = SessionLocal()
    data = db.query(Interaction).all()
    return data