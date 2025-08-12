from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from app.data.data import walks

mainRouter = APIRouter()

templates = Jinja2Templates(directory="templates")

@mainRouter.get("/", response_class=HTMLResponse)
async def home_section(request: Request):
    return templates.TemplateResponse("pages/home.jinja", {"request": request})


@mainRouter.get("/about", response_class=HTMLResponse)
async def about_section(request: Request):
    return templates.TemplateResponse("pages/about.jinja", {"request": request})


@mainRouter.get(path="/walks", response_class=HTMLResponse)
async def walks_section(request: Request):
    context = {"request": request, "walks": walks}
    return templates.TemplateResponse("pages/walks.jinja", context)


@mainRouter.get(path="/blog", response_class=HTMLResponse)
async def blog_section(request: Request):
    return templates.TemplateResponse("pages/blog.jinja", {"request": request})


@mainRouter.get("/json", response_class=JSONResponse)
async def json_example():
    return {"Hello": "World"}
