from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_db

router = APIRouter()

@router.get("/health")
async def health(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    return {"db_status": "ok" if result.scalar() == 1 else "error"}