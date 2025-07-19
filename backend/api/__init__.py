from __future__ import annotations

from fastapi import APIRouter
from .auth import router as auth_router

__all__ = ["main_router"]

main_router = APIRouter(prefix="/api", tags=["main"])
main_router.include_router(auth_router, prefix="/auth", tags=["auth"])
