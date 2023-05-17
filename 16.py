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
    pilha = Pilha()
    while num > 0:
        resto = num % 16
        if resto < 10:
            pilha.inserir(resto)
        else:
            if resto == "A":
                pilha.inserir(10)
            elif resto == "B":
                pilha.inserir(11)
            elif resto == "C":
                pilha.inserir(12)
            elif resto == "D":
                pilha.inserir(13)
            elif resto == "E":
                pilha.inserir(14)
            elif resto == "F":
                pilha.inserir(15)
        num = num // 16
    return pilha
 
num = input("\nDigite um número em Decimal: ")
resto = converter(num)

print("\nEm Hexadecimal é: ")
while not resto.is_empty():
    print(resto.remover())