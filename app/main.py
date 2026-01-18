from fastapi import FastAPI
from app.api.routes import router
from app.api.tree_router import router as tree_router

app = FastAPI(title='Decision Engine')

#app.include_router(router)
app.include_router(tree_router)

