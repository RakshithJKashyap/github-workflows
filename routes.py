from connect_database import session
from fastapi import APIRouter

# session.execute("""
#     CREATE TABLE learn.police (
#         id INT PRIMARY KEY,
#         name TEXT,
#         badge_number TEXT
#     )
# """)

router = APIRouter()

@router.post("/")
async def create_police(id: int, name: str, badge_number: str):
    statement = session.prepare("INSERT INTO learn.police (id, name, badge_number) VALUES (?, ?, ?)")
    session.execute(statement, (id,name,badge_number))
    return {"message": "Police record created successfully"}

@router.get("/{id}")
async def get_police(id: int):
    statement = session.prepare("SELECT id, name, badge_number FROM learn.police WHERE id = ?")
    result = session.execute(statement, (id,))
    police_data = result.one()
    if police_data:
        return police_data._asdict()
    else:
        return {"message": "Police record not found"}

@router.put("/{id}")
async def update_police(id: int, name: str, badge_number:str):
    statement = session.prepare("UPDATE learn.police SET name = ?, badge_number = ? WHERE id = ?")
    session.execute(statement, (name, badge_number, id))
    return {"message": "Police record updated successfully"}

@router.delete("/{id}")
async def delete_police(id: int):
    statement = session.prepare("DELETE FROM learn.police WHERE id = ?")
    session.execute(statement, (id,))
    return {"message": "Police record deleted successfully"}

