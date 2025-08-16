from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.config import templates
from app.data.walks import walks

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home_section(request: Request):
    return templates.TemplateResponse("pages/home.jinja", {"request": request})


@router.get("/about", response_class=HTMLResponse)
async def about_section(request: Request):
    return templates.TemplateResponse("pages/about.jinja", {"request": request})


@router.get(path="/walks", response_class=HTMLResponse)
async def walks_section(request: Request):
    context = {"request": request, "walks": walks}
    return templates.TemplateResponse("pages/walks.jinja", context)


@router.get(path="/blog", response_class=HTMLResponse)
async def blog_section(request: Request):
    return templates.TemplateResponse("pages/blog.jinja", {"request": request})
