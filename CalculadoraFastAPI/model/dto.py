class CalcInput:  #Criando a classe que sera o input e o parâmetro da calculadora
    valor_1: int
    valor_2: int

    def __init__(self, valor_1:int, valor_2:int): #__init__ é equivalente a um construtor em java
        self.valor_1 = valor_1
        self.valor_2 = valor_2