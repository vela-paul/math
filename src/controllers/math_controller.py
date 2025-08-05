from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import logging 

from models.schemas import *
from services.math_service import *
from repositories.request_repo import *
from db.session import get_db

router = APIRouter(
    prefix="",
    tags=["math-operations"]
)

@router.post("/pow", response_model=MathResponse)
def pow_endpoint(req: PowRequest, db: Session = Depends(get_db)):
    try:
        result = compute_pow(req.base, req.exponent)
        # persist request
        log_request(db, OperationType.POW, req.dict(), result)
        return MathResponse(
            operation=OperationType.POW,
            parameters=req.dict(),
            result=result
        )
    except HTTPException:
        raise
    except Exception:
        logging.error("Error in pow_endpoint", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/fib", response_model=MathResponse)
def fib_endpoint(req: FibRequest, db: Session = Depends(get_db)):
    try:
        result = compute_fib(req.n)
        log_request(db, OperationType.FIB, req.dict(), result)
        return MathResponse(
            operation=OperationType.FIB,
            parameters=req.dict(),
            result=result
        )
    except HTTPException:
        raise
    except Exception:
        logging.error("Error in fib_endpoint", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/factorial", response_model=MathResponse)
def factorial_endpoint(req: FactorialRequest, db: Session = Depends(get_db)):
    try:
        result = compute_factorial(req.n)
        log_request(db, OperationType.FACTORIAL, req.dict(), result)
        return MathResponse(
            operation=OperationType.FACTORIAL,
            parameters=req.dict(),
            result=result
        )
    except HTTPException:
        raise
    except Exception:
        logging.error("Error in factorial_endpoint", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
