from database import SessionLocal
from models import Interaction

# 1. Log Interaction
def log_interaction(data):
    db = SessionLocal()
    interaction = Interaction(**data)
    db.add(interaction)
    db.commit()
    return {"status": "logged"}

# 2. Edit Interaction
def edit_interaction(data):
    db = SessionLocal()
    obj = db.query(Interaction).filter(Interaction.id == data["id"]).first()
    setattr(obj, data["field"], data["new_value"])
    db.commit()
    return {"status": "updated"}

# 3. Fetch Insights
def fetch_insights(hcp_name):
    db = SessionLocal()
    data = db.query(Interaction).filter(Interaction.hcp_name == hcp_name).all()
    return {"history": [d.notes for d in data]}

# 4. Suggest Next Action
def suggest_action(data):
    return {"suggestion": "Follow up in 2 weeks"}

# 5. Compliance Check
def compliance_check(text):
    if "off-label" in text.lower():
        return {"warning": "Non-compliant content"}
    return {"status": "ok"}