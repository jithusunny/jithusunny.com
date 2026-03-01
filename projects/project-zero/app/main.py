from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from components.api_thoughts import router as thoughts_router

PER_PAGE = 7

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "components" / "ui_shell" / "static"), name="static")

template_dirs = [
    BASE_DIR / "components" / "ui_thought_list" / "templates",
    BASE_DIR / "components" / "ui_thought_form" / "templates",
    BASE_DIR / "components" / "ui_thought_read" / "templates",
]
templates = Jinja2Templates(directory=str(template_dirs[0]))
templates.env.loader.searchpath = [str(d) for d in template_dirs]

app.state.templates = templates
app.state.per_page = PER_PAGE

app.include_router(thoughts_router, tags=["thoughts"])
