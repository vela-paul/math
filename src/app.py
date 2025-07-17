from fastapi import FastAPI
from db.session import engine, Base
from controllers.math_controller import router as math_router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Math Ops Service")
app.include_router(math_router)
