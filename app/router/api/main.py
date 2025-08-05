from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

mainRouter = APIRouter()

templates = Jinja2Templates(directory="templates")

@mainRouter.get("/", response_class=HTMLResponse)
async def home_section(request: Request):
    return templates.TemplateResponse("pages/home.jinja", {"request": request})


@mainRouter.get("/about", response_class=HTMLResponse)
async def about_section(request: Request):
    return templates.TemplateResponse("pages/about.jinja", {"request": request})


@mainRouter.get(path="/categories", response_class=HTMLResponse)
async def categories_section(request: Request):
    return templates.TemplateResponse("pages/categories.jinja", {"request": request})


@mainRouter.get("/json", response_class=JSONResponse)
async def json_example():
    return {"Hello": "World"}
