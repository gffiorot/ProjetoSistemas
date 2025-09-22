from fastapi import FastAPI
from controller.control_calc import router as calcRouter

app = FastAPI(title="Calculadora + FastAPI + MVC")
app.include_router(calcRouter)

app.get("/")
def health():
    return {"status": "Calculadora funcionando."}