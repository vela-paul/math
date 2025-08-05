import logging
from fastapi import FastAPI  # type: ignore
from db.session import engine, Base  # type: ignore
from controllers.math_controller import router as math_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

app = FastAPI(title="Math Ops Service")
@app.on_event("startup")
def check_migrations():
    #no migrations for now
    pass
app.include_router(math_router)
