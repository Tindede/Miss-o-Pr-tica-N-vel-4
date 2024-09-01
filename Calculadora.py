class Calculadora:
    def __init__(self, valorA=0, valorB=0, operacao='+'):
        self.__valorA = valorA
        self.__valorB = valorB
        self.__operacao = operacao

    @property
    def valorA(self):
        return self.__valorA

    @valorA.setter
    def valorA(self, valorA):
        self.__valorA = valorA

    @property
    def valorB(self):
        return self.__valorB

    @valorB.setter
    def valorB(self, valorB):
        self.__valorB = valorB

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao

    def validarOperacao(self, operacao):
        """Valida se a operação é uma das operações matemáticas permitidas."""
        return operacao in ['+', '-', '*', '/']

    def calcular(self):
        """Executa o cálculo baseado na operação definida."""
        if not self.validarOperacao(self.__operacao):
            print("Operação inválida.")
            exit() 

        if self.__operacao == '+':
            return self.__valorA + self.__valorB
        elif self.__operacao == '-':
            return self.__valorA - self.__valorB
        elif self.__operacao == '*':
            return self.__valorA * self.__valorB
        elif self.__operacao == '/':
            if self.__valorB == 0:
                print("Não é possível dividir por zero.")
                exit()  
            return self.__valorA / self.__valorB

    def mostrarResultado(self):
        """Mostra o resultado da operação."""
        print(f"{self.__valorA} {self.__operacao} {self.__valorB} = {self.calcular()}")

    def entrada_dados(self):
        """Permite a entrada de dados via prompt."""
        try:
            self.__valorA = float(input("Digite o valor A: "))
            self.__valorB = float(input("Digite o valor B: "))
            self.__operacao = input("Digite a operação (+, -, *, /): ").strip()
        except ValueError:
            print("Valor inválido inserido.")
            exit() 

            