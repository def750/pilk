from contextlib import asynccontextmanager

import uvicorn
from datetime import timedelta
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from api import main_router
from settings import Config
from core.db import create_db_and_tables

# from backend.routes.middlewares import MetricsMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    # Code to run on startup
    # logger.info("Uruchamianie Backendu...")
    # ensure_persistent_volumes_are_available()
    # api.state.services.redis = await redis.Redis(
    #     host=api.settings.REDIS_HOST,
    #     port=api.settings.REDIS_PORT,
    #     db=api.settings.REDIS_DB,
    #     password=api.settings.REDIS_PASS,
    #     # username=api.settings.REDIS_USER,
    #     retry_on_timeout=True,
    #     protocol=3,
    # )
    # logger.info("Połączenie z Redis zostało nawiązane")

    yield
    # # Code to run on shutdown
    # logger.info("Wyłączanie backendu...")
    # await api.state.services.redis.aclose()
    # logger.info("Połączenie z Redis zostało zamknięte")
    # # await api.state.services.database.disconnect()


# app.add_middleware(MetricsMiddleware)


"""
Main entry point for the FastAPI application.
"""
app = FastAPI(
    title="Pilk",
    description="Pilk API",
    docs_url="/api/py/docs",
    openapi_url="/api/py/openapi.json",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        f"{Config.Service.Frontend.host}:{Config.Service.Frontend.port}",  # e.g., "http://localhost:3000"
        f"{Config.General.domain}",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    SessionMiddleware,
    secret_key=Config.Service.Backend.secret_key,
    cookie_name="session",
    max_age=timedelta(days=30).total_seconds(),
    same_site="lax",
)
# Register routers
app.include_router(main_router)


if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host=Config.Service.Backend.host,
        port=Config.Service.Backend.port,
        reload=Config.General.debug,
    )

# app.add_exception_handler(Exception, internal_server_error_handler)
# app.add_exception_handler(404, not_found_handler)
