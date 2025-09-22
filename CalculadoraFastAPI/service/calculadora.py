from model.dto import CalcInput
class Calculadora:
    def somar (self, data: CalcInput) -> float:
        return data.valor_1 + data.valor_2
    
    def subtrair (self, data: CalcInput) -> float:
        return data.valor_1 - data.valor_2
    
    def multiplicar (self, data: CalcInput) -> float:
        return data.valor_1 * data.valor_2
    
    def dividir (self, data: CalcInput) -> float:
        return data.valor_1 / data.valor_2
    