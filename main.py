from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routes import home_routes

app = FastAPI()

# Configuración de las vistas
templates = Jinja2Templates(directory="views")

# Rutas
app.include_router(home_routes.router)
