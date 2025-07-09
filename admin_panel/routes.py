
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlite3

router = APIRouter()
templates = Jinja2Templates(directory="admin_panel/templates")

@router.get("/admin/users", response_class=HTMLResponse)
async def list_users(request: Request):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users ORDER BY joined_at DESC")
    users = c.fetchall()
    conn.close()
    return templates.TemplateResponse("dashboard.html", {"request": request, "users": users})
