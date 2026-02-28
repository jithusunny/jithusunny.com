from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from storage import list_thoughts, read_thought, save_thought

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    thoughts = list_thoughts()
    return templates.TemplateResponse("home.html", {"request": request, "thoughts": thoughts})


@app.get("/add", response_class=HTMLResponse)
async def add_page(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})


@app.post("/add")
async def add_thought(content: str = Form(...)):
    save_thought(content)
    return RedirectResponse(url="/", status_code=303)


@app.get("/thought/{path:path}", response_class=HTMLResponse)
async def read_page(request: Request, path: str):
    thought = read_thought(path)
    if thought is None:
        return HTMLResponse("<h1>Not found</h1>", status_code=404)
    return templates.TemplateResponse("read.html", {"request": request, "thought": thought})
