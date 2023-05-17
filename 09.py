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
    
def verifica_palindromo_numero(string):
    pi = Pilha() 

    for digito in string:
        pi.inserir(digito)

    string_invertida = ""
    while not pi.is_empty():
        string_invertida += pi.remover()

    return string == string_invertida

string = input("Digite um número: ")
if verifica_palindromo_numero(string):
    print("O número é um palíndromo")
else:
    print("O número não é um palíndromo")
