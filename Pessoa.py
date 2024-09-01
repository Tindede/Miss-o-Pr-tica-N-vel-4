from datetime import datetime

class Pessoa:
    def __init__(self, nome, numeroConta, dataAberturaConta, status=False):
        self.__nome = nome
        self.__numeroConta = numeroConta
        self.__dataAberturaConta = dataAberturaConta
        self.__status = status

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def numeroConta(self):
        return self.__numeroConta

    @numeroConta.setter
    def numeroConta(self, numeroConta):
        self.__numeroConta = numeroConta

    @property
    def dataAberturaConta(self):
        return self.__dataAberturaConta

    @dataAberturaConta.setter
    def dataAberturaConta(self, dataAberturaConta):
        self.__dataAberturaConta = dataAberturaConta

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    def imprimir_informacoes(self):
        print(f"Nome: {self.__nome}")
        print(f"Número da Conta: {self.__numeroConta}")
        print(f"Data de Abertura da Conta: {self.__dataAberturaConta}")
        print(f"Status: {self.__status}")