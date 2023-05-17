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
    
def verifica_balanceamento(string):
    pi = Pilha()

    for caractere in string:
        if caractere in "([{":
            pi.inserir(caractere)
        elif caractere in ")]}":
            if pi.is_empty():
                return False
            topo = pilha.remover()
            if (caractere == ')' and topo != '(') or \
               (caractere == ']' and topo != '[') or \
               (caractere == '}' and topo != '{'):
                return False

    return pi.is_empty()

string = input("Digite uma string: ")
if verifica_balanceamento(string):
    print("Os caracteres estão balanceados")
else:
    print("Os caracteres não estão balanceados")
