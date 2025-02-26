from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

#fila_teste = FilaNormal()
#fila_teste.atualiza_fila()
#fila_teste.atualiza_fila()
#fila_teste.atualiza_fila()

#print(fila_teste.chamar_cliente(5))
#print(fila_teste.chamar_cliente(5))
#print(fila_teste.chamar_cliente(15))

fila_teste = FilaPrioritaria()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()

print(fila_teste.chamar_cliente(5))
print(fila_teste.chamar_cliente(15))
print(fila_teste.estatistica('10/01/2025', 198, 'detail'))