from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from controllers import home_controller

app = FastAPI()

# Configuración de las vistas
templates = Jinja2Templates(directory="views")

# Ruta principal delegada al controlador
app.include_router(home_controller.router)
