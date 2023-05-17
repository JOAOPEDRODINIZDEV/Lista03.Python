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

def converter(num):
    pi = Pilha()
    while num > 0:
        resto = num % 16
        if resto < 10:
            pi.inserir(resto)
        else:
            if resto == 10:
                pi.inserir("A")
            elif resto == 11:
                pi.inserir("B")
            elif resto == 12:
                pi.inserir("C")
            elif resto == 13:
                pi.inserir("D")
            elif resto == 14:
                pi.inserir("E")
            elif resto == 15:
                pi.inserir("F")
        num = num // 16
    return pi
 
num = int(input("\nDigite um número em Decimal: "))
resto = converter(num)

print("\nEm Hexadecimal é: ")
while not resto.is_empty():
    print(resto.remover())