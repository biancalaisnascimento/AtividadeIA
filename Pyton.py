from aima.logic import *

# Definindo os símbolos proposicionais
A = Symbol("A")
B = Symbol("B")

# Definindo as cláusulas da base de conhecimento
base_conhecimento = And(
    Implication(A, B),
    Not(B)
)

# Função para resolver as cláusulas usando a resolução de refutação
def resolver(base_conhecimento):
    return pl_resolution(base_conhecimento, B)

# Verificando se B é verdade dado a base de conhecimento
resultado = resolver(base_conhecimento)

if resultado:
    print("B é verdadeiro dado a base de conhecimento.")
else:
    print("B é falso dado a base de conhecimento.")
