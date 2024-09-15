from fastapi import FastAPI
from .routers import users, operations, bids

app = FastAPI()

app.include_router(users.router)
app.include_router(operations.router)
app.include_router(bids.router)
