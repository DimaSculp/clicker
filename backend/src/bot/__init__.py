from aiogram import Router

from . import handlers

def settup_routes() -> Router:
    router = Router()
    router.include_router(handlers.router)
    return router