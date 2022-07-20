# decorador
def timer(f, *args, **kwargs):
    def modificada():
        # o que vou colocar aqui dentro vai modificar
        start = time.time()
        # executar a funcao original
        f()
        end = time.time()
        print(f'Essa funcao demorou {end - start} segundos')
    return modificada

@timer
def funcaoa():
     for i in range(100_000_000):
         a = 2*20
@timer
def funcaob():
    for i in range(100_000_000):
        a = 2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2

import time

start = time.time()
funcaoa()
end = time.time()

print(f'a funcao demorou {end - start} segundos')

start = time.time()
funcaob()
end = time.time()

print(f'a funcao demorou {end - start} segundos')


# da maneira inteligente com decorator:
print('decorator used')
funcaoa()