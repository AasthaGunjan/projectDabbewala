from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables
import uvicorn

from routes.orders import router as order_router
from routes.stats import router as stat_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Database tables created.")
    yield
    print("Application shutdown.")

app = FastAPI(

    title="Dabbewala delivery API",
    description="API for managing dabbawala deliveries and tracking order statuses.",
    version="1.0.0",
    lifespan=lifespan

)

app.include_router(order_router)
app.include_router(stat_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, workers=1)