# pyright: reportUnknownMemberType=false
import arel
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.config import DEBUG, templates
from app.api import pages, client

app = FastAPI(title="Caminatas")
app.mount("/static", StaticFiles(directory="static"), name="static")

if DEBUG:
    hot_reload = arel.HotReload(
        paths=[arel.Path("templates"), arel.Path("static/input.css")]
    )

    async def hot_reload_wrapper(websocket: WebSocket):
        await hot_reload(websocket.scope, websocket.receive, websocket.send)

    app.add_websocket_route(
        "/hot-reload", route=hot_reload_wrapper, name="hot-reload"
    )

    # annoying warnings related to unknow types from libraries
    app.add_event_handler("startup", hot_reload.startup)
    app.add_event_handler("shutdown", hot_reload.shutdown)
    templates.env.globals["DEBUG"] = True
    templates.env.globals["hot_reload"] = hot_reload

app.add_middleware(
    SessionMiddleware,
    secret_key="helosdfaslkdjfalskdjfalskjdf",
    https_only=True,
)
app.include_router(pages.router)
app.include_router(client.router)
