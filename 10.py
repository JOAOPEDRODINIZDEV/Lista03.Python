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
    
     
def infixa_para_posfixa(expresão):
    operadores = Pilha()
    posfixa = []
    numeros = '0123456789'
    for carater in numeros:
        if carater in numeros:
            posfixa.append(carater)
        elif carater == '(':
            operadores.inserir(carater)
        elif carater in precedencia:
            while not operadores.is_empty() \
                and operadores.topo() != '(' \
                and precedencia[carater] <= precedencia[operadores.topo]:
                posfixa.append(operadores.remover())
            operadores.inserir(carater)
    while not operadores.is_empty():
        posfixa.append(operadores.remover())
    return ''.join(posfixa)

def calcular(exp):
    pi = Pilha()
    for c in exp:
        if c.isdigit():
            pi.inserir(int(c))
        elif c in "+-*/":
            b = pi.remover()
            a = pi.remover()
            if c == "+":
                pi.inserir(a + b)
            elif c == "-":
                pi.inserir(a - b)
            elif c == "*":
                pi.inserir(a * b)
            elif c == "/":
                pi.inserir(a / b)
    return pi.remover()


s = input("Digite uma expressão matemática na notação polonesa reversa: ")

posfixa = infixa_para_posfixa(s)

r = calcular(posfixa)

print("Resultado: ",r)
             
         