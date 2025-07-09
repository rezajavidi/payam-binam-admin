from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Mount static folder (empty for now, can add css/js later)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="templates")

# Simple username/password credentials
USERNAME = os.getenv("ADMIN_USERNAME", "admin")
PASSWORD = os.getenv("ADMIN_PASSWORD", "Salam@123")

def verify_credentials(username: str, password: str):
    if username != USERNAME or password != PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/", response_class=HTMLResponse)
async def login_form(request: Request):
    """Render login page."""
    return templates.TemplateResponse("login.html", {"request": request, "error": None})

@app.post("/admin", response_class=HTMLResponse)
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):
    """Process login credentials and render dashboard."""
    try:
        verify_credentials(username, password)
        return templates.TemplateResponse("dashboard.html", {"request": request, "username": username})
    except HTTPException:
        return templates.TemplateResponse("login.html", {"request": request, "error": "❌ نام کاربری یا رمز عبور اشتباه است!"})