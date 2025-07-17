from sqlalchemy.orm import Session
from models.schemas import OperationType
from db.session import get_db, Base
from sqlalchemy import Column, Integer, String


class RequestRepository(Base):
    __tablename__ = 'requests_logs'
    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, nullable=False)
    parameters = Column(String, nullable=False)
    result = Column(Integer, nullable=False)
    created_at = Column(String, nullable=False)

def log_request(db: Session, operation: OperationType, parameters: dict, result: int):
    request_log = RequestRepository(
        operation=operation.value,
        parameters=str(parameters),
        result=result,
        created_at='now()'  # This should be replaced with actual timestamp logic
    )
    db.add(request_log)
    db.commit()
    db.refresh(request_log)
    return request_log