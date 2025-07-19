import authlib
import datetime
from sqlalchemy import String, func, DateTime, Uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import mapped_column
from uuid import uuid4

from models import Base
from core.db import get_async_session


class User(Base):
    __tablename__ = "user"

    id = mapped_column(Uuid, primary_key=True, default=uuid4)
    username = mapped_column(String(32), unique=True, index=True)
    email = mapped_column(String(255), unique=True, index=True)
    password_hash = mapped_column(String(255), nullable=False)
    join_date = mapped_column(DateTime, default=func.now)
