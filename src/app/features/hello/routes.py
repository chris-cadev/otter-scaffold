from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.core.responses import create_templates
from app.features.hello.services import get_greetings, create_greeting

router = APIRouter()

templates = create_templates([
    Path("src/app/features/hello/templates"),
])


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    greetings = await get_greetings()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "greetings": greetings}
    )


@router.post("/", response_class=HTMLResponse)
async def create_greeting_handler(request: Request):
    form = await request.form()
    name = form.get("name", "Anonymous")
    message = form.get("message", "")

    if message.strip():
        await create_greeting(name, message)

    greetings = await get_greetings()
    return templates.TemplateResponse(
        "greeting_list.html",
        {"request": request, "greetings": greetings}
    )
