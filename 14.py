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

def converter_para_polonesa_reversa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    resultado = []

    for token in expressao:
        if token.isdigit():
            resultado.append(token)
        elif token in precedencia:
            while (not operadores.is_empty() and
                   operadores.topo() != '(' and
                   precedencia[token] <= precedencia[operadores.topo()]):
                resultado.append(operadores.remover())
            operadores.inserir(token)
        elif token == '(':
            operadores.inserir(token)
        elif token == ')':
            while not operadores.is_empty() and operadores.topo() != '(':
                resultado.append(operadores.remover())
            if operadores.is_empty():
                raise ValueError("Expressão inválida: parênteses desbalanceados")
            operadores.remover()

    while not operadores.is_empty():
        if operadores.topo() == '(':
            raise ValueError("Expressão inválida: parênteses desbalanceados")
        resultado.append(operadores.remover())

    return ' '.join(resultado)

# Exemplo de uso
expressao = input("Digite uma expressão matemática: ")
polonesa_reversa = converter_para_polonesa_reversa(expressao)
print("Notação polonesa reversa:", polonesa_reversa)
