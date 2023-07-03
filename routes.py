from fastapi import APIRouter
from pydantic import BaseModel
from cassandra.query import SimpleStatement
from connect_database import get_session

router = APIRouter()
session = get_session()

# session.execute("""
#     CREATE TABLE learn.police_records (
#         id TEXT PRIMARY KEY,
#         name TEXT,
#         badge_number TEXT,
#         department TEXT
#     )
# """)

class PoliceRecord(BaseModel):
    id: str
    name: str
    badge_number: str
    department: str


@router.post("/records")
async def create_record(record: PoliceRecord):
    query = "INSERT INTO learn.police_records (id, name, badge_number, department) VALUES (?, ?, ?, ?)"
    prepared = session.prepare(query)
    session.execute(prepared, (record.id, record.name, record.badge_number, record.department))
    return {"message": "Record created successfully"}


@router.get("/records/{record_id}")
async def get_record(record_id: str):
    query = "SELECT * FROM learn.police_records WHERE id = ?"
    prepared = session.prepare(query)
    result = session.execute(prepared, (record_id,))
    record = result.one()
    if record:
        return record_to_dict(record)
    else:
        return {"message": "Record not found"}


@router.put("/records/{record_id}")
async def update_record(record_id: str, updated_record: PoliceRecord):
    query = "UPDATE learn.police_records SET name = ?, badge_number = ?, department = ? WHERE id = ?"
    prepared = session.prepare(query)
    session.execute(prepared, (updated_record.name, updated_record.badge_number,
                               updated_record.department, record_id))
    return {"message": "Record updated successfully"}


@router.delete("/records/{record_id}")
async def delete_record(record_id: str):
    query = "DELETE FROM learn.police_records WHERE id = ?"
    prepared = session.prepare(query)
    session.execute(prepared, (record_id,))
    return {"message": "Record deleted successfully"}


def record_to_dict(record):
    return {
        "id": record.id,
        "name": record.name,
        "badge_number": record.badge_number,
        "department": record.department
    }