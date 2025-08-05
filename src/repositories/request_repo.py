from sqlalchemy.orm import Session # type: ignore
from models.schemas import OperationType
from db.session import Base
from sqlalchemy import Column, Integer, String, DateTime, JSON # type: ignore
from datetime import datetime


class RequestRepository(Base):
    __tablename__ = 'requests_logs'
    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, nullable=False)
    parameters = Column(JSON, nullable=False)
    result = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

def log_request(db: Session, operation: OperationType, parameters: dict, result: str):
    request_log = RequestRepository(
        operation=operation.value,
        parameters=parameters,
        result=result,
        created_at=datetime.utcnow()
    )
    db.add(request_log)
    db.commit()
    db.refresh(request_log)
    return request_log