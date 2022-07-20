# iterates over the object

listaA = ['a','b','c','d','e']

iter_listaA = iter(listaA)

try:
    print(next(iter_listaA))
except:
    print('no next element')
