from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

USERNAME = os.getenv("ADMIN_USERNAME", "admin")
PASSWORD = os.getenv("ADMIN_PASSWORD", "Salam@123")

# ---------- صفحهٔ لاگین (GET) ----------
@app.get("/", response_class=HTMLResponse)
@app.get("/admin", response_class=HTMLResponse)   # ← این خط تازه اضافه شد
async def login_form(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": None}
    )

# ---------- پردازش فرم لاگین (POST) ----------
@app.post("/admin", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == USERNAME and password == PASSWORD:
        return templates.TemplateResponse(
            "dashboard.html",
            {"request": request, "username": username}
        )
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": "❌ نام کاربری یا رمز عبور اشتباه است!"}
    )
