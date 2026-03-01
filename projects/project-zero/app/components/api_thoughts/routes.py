from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse

from components.storage_fs import list_thoughts, read_thought, save_thought

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request, page: int = 1):
    if page < 1:
        page = 1
    templates = request.app.state.templates
    per_page = request.app.state.per_page
    thoughts, total = list_thoughts(page=page, per_page=per_page)
    has_prev = page > 1
    has_next = page * per_page < total
    return templates.TemplateResponse("home.html", {
        "request": request,
        "thoughts": thoughts,
        "page": page,
        "has_prev": has_prev,
        "has_next": has_next,
    })


@router.get("/add", response_class=HTMLResponse)
async def add_page(request: Request):
    return request.app.state.templates.TemplateResponse("add.html", {"request": request})


@router.post("/add")
async def add_thought(content: str = Form(...)):
    save_thought(content)
    return RedirectResponse(url="/", status_code=303)


@router.get("/thought/{path:path}", response_class=HTMLResponse)
async def read_page(request: Request, path: str):
    thought = read_thought(path)
    if thought is None:
        return HTMLResponse("<h1>Not found</h1>", status_code=404)
    return request.app.state.templates.TemplateResponse("read.html", {
        "request": request,
        "thought": thought,
    })
