from fastapi import APIRouter


router =APIRouter(
    prefix="/health",
    tags=["Health"]
)

@router.get("/")
def health():
    return {
        "status":"Backend Running",
        "database" : "for database check database session "
    }