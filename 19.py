class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self._topo = None
        self.tamanho = 0
   
    def __len__(self):
        return self.tamanho
   
    def is_empty(self):
        return self.tamanho == 0
   
    def inserir(self, valor):
        no = No(valor)
        no.proximo = self._topo
        self._topo = no
        self.tamanho += 1
   
    def remover(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self.tamanho -= 1
        return valor
   
    def topo(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self._topo.valor
    
def binario_para_octal(binario):
    decimal = binario_para_decimal(binario)
    octal = decimal_para_octal(decimal)
    return octal

def binario_para_decimal(binario):
    pilha = Pilha()
    for digito in binario:
        pilha.inserir(int(digito))
    
    decimal = 0
    potencia = 0

    while not pilha.is_empty():
        digito = pilha.remover()
        decimal += digito * (2 ** potencia)
        potencia += 1

    return decimal

def decimal_para_octal(decimal):
    pi = Pilha()
    
    if decimal == 0:
        pilha.inserir(0)
    
    while decimal > 0:
        resto = decimal % 8
        pi.inserir(resto)
        decimal //= 8

    octal = ""
    while not pi.is_empty():
        digito = pi.remover()
        octal += str(digito)
    
    return octal

binario = input("Digite um número binário: ")
octal = binario_para_octal(binario)
print("Número convertido em octal:", octal)
