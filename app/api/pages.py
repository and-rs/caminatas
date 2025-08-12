from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.data.walks import walks
from app.services.image_cycler import create_image_cycler

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def home_section(request: Request):
    return templates.TemplateResponse("pages/home.jinja", {"request": request})


get_next_image = create_image_cycler()


@router.get("/carousel", response_class=HTMLResponse)
def carousel_fragment():
    src = get_next_image()
    return Response(
        content=f'<img src="{src}" class="object-cover w-full h-full" loading="lazy">',
        media_type="text/html",
    )


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
