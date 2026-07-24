from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.database import router as database_router
from app.api.users import router as users_router
from app.api.projects import router as project_router
from app.api.upload import router as upload_router
from app.database.database import Base,engine

Base.metadata.create_all(bind=engine)



app = FastAPI(
    title="AI Sales Forecast Dashboard API",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router (database_router)
app.include_router (users_router)
app.include_router(project_router)
app.include_router(upload_router)

@app.get("/")
def root():
    return {
        "message": "AI Sales Forecast Dashboard Backend Running Successfully"
    }


