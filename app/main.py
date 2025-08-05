import arel
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.config import DEBUG
from app.router.api import main

app = FastAPI(title="Caminatas")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

if DEBUG:
    hot_reload = arel.HotReload(
        paths=[arel.Path("templates"), arel.Path("static/input.css")]
    )

    async def hot_reload_wrapper(websocket: WebSocket):
        await hot_reload(websocket.scope, websocket.receive, websocket.send)

    app.add_websocket_route(
        "/hot-reload", route=hot_reload_wrapper, name="hot-reload"
    )
    app.add_event_handler("startup", hot_reload.startup)
    app.add_event_handler("shutdown", hot_reload.shutdown)
    templates.env.globals["DEBUG"] = True
    templates.env.globals["hot_reload"] = hot_reload

app.include_router(main.mainRouter)