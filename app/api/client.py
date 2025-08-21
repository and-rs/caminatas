from fastapi import Request, Response
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter

from app.config import templates

router: APIRouter = APIRouter()


CAROUSEL_IMAGES: list[str] = [
    "/static/images/bg1.png",
    "/static/images/forest.jpg",
    "/static/images/trail.jpg",
    "/static/images/trees.jpg",
]


@router.get(path="/carousel", response_class=HTMLResponse)
def carousel_fragment(request: Request) -> Response:
    current_index: int = request.session.get("image_index", 0)
    src: str = CAROUSEL_IMAGES[current_index]
    next_index: int = (current_index + 1) % len(CAROUSEL_IMAGES)
    request.session["image_index"] = next_index
    return Response(
        content=f'<img src="{src}" class="object-cover w-full h-full" loading="lazy">',
        media_type="text/html",
    )


@router.get(path="/toggle-mobile-modal", response_class=HTMLResponse)
async def toggle_sidebar(request: Request):
    current_visible: bool = request.session.get("mobile_menu_visible", False)
    visible: bool = not current_visible
    request.session["mobile_menu_visible"] = visible
    return templates.TemplateResponse(
        "partials/mobile-modal.jinja", {"request": request, "visible": visible}
    )
