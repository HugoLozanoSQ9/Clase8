def decorator2(func):
    def wrapper():
        print('Este es otro decorador')
        func()
    return wrapper

def decorador1(func):
    def wrapper():
        print('La función se está inicializando')
        func()
        print('La función está finalizando')
    return wrapper


@decorador1
@decorator2
def hello_k():
    print('Hello Koders')

@decorador1
def hello_w():
    print('Hello world')

hello_k()
hello_w()

# wrapper(hello_k) 
# wrapper(hello_w)

