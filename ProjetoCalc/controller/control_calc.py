from fastapi import APIRouter
from model.dto import CalcInput
from service.calculadora import Calculadora

router = APIRouter(tags=["Calculadora"])

calc = Calculadora()

@router.get("/somar/{valor_1}/{valor_2}")
async def somar(valor_1: int, valor_2: int):
    data = CalcInput(valor_1, valor_2)
    return {"Resultado": calc.somar(data)}

@router.get("/subtrair/{valor_1}/{valor_2}")
async def subtrair(valor_1: int, valor_2: int):
    data = CalcInput(valor_1, valor_2)
    return {"Resultado": calc.subtrair(data)}

@router.get("/multiplicar/{valor_1}/{valor_2}")
async def multiplicar(valor_1: int, valor_2: int):
    data = CalcInput(valor_1, valor_2)
    return {"Resultado": calc.multiplicar(data)}

@router.get("/dividir/{valor_1}/{valor_2}")
async def dividir(valor_1: int, valor_2: int):
    if valor_2 == 0:
            raise ValueError("Divisão por zero!")
    
    data = CalcInput(valor_1, valor_2)
    return {"Resultado": calc.dividir(data)}
    