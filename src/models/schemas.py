from pydantic import BaseModel, Field
from enum import Enum


class OperationType(str, Enum):
    POW = 'pow'
    FIB = 'fib'
    FACTORIAL = 'factorial'


class PowRequest(BaseModel):
    base: int = Field(..., description="The base integer to raise to a power")
    exponent: int = Field(..., description="The exponent integer")


class FibRequest(BaseModel):
    n: int = Field(..., ge=0, description="The zero-based index of the Fibonacci sequence to compute")


class FactorialRequest(BaseModel):
    n: int = Field(..., ge=0, description="The non-negative integer to compute the factorial of")


class MathRequest(BaseModel):
    operation: OperationType = Field(..., description="Type of mathematical operation")
    parameters: dict = Field(..., description="Parameters for the operation")


class MathResponse(BaseModel):
    operation: OperationType = Field(..., description="Type of mathematical operation performed")
    parameters: dict = Field(..., description="Parameters used for the operation")
    result: int = Field(..., description="Result of the computation")