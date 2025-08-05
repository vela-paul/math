from pydantic import BaseModel, Field # type: ignore
from enum import Enum


class OperationType(str, Enum):
    POW = 'pow'
    FIB = 'fib'
    FACTORIAL = 'factorial'


class PowRequest(BaseModel):
    base: int = Field(..., description="The base integer to raise to a power")
    exponent: int = Field(
        ..., ge=0, le=1000,
        description="The exponent integer (0–1000)"
    )


class FibRequest(BaseModel):
    n: int = Field(
        ..., ge=0, le=10000,
        description="The zero-based index of the Fibonacci sequence to compute (0–10000)"
    )


class FactorialRequest(BaseModel):
    n: int = Field(
        ..., ge=0, le=10000,
        description="The non-negative integer to compute the factorial of (0–10000)"
    )


class MathRequest(BaseModel):
    operation: OperationType = Field(..., description="Type of mathematical operation")
    parameters: dict = Field(..., description="Parameters for the operation")


class MathResponse(BaseModel):
    operation: OperationType = Field(..., description="Type of mathematical operation performed")
    parameters: dict = Field(..., description="Parameters used for the operation")
    result: str = Field(..., description="Result of the computation")