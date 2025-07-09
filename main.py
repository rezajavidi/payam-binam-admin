
from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

USERNAME = "admin"
PASSWORD = "Salam@123"

def check_credentials(username: str = Form(...), password: str = Form(...)):
    if username != USERNAME or password != PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return True

@app.get("/", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/admin", response_class=HTMLResponse)
async def login(
    request: Request,
    valid: bool = Depends(check_credentials)
):
    return templates.TemplateResponse("dashboard.html", {"request": request})
