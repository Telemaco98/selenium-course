### Search for yield (Generators)
# Generated funcions
def name(args):
    yield args

### Search for lambda
# Anonymous functions
lambda args: op(args)

# =============================================================
# ====================== Named functions ======================
# =============================================================

def name(args):
    return args

# Pattern
def func(a, b = 1, *c, **d):        # *c = Empacotador, **d = Dictionary
    return a, b, c, d

func(*[1, 2, 3, 4, 5], x = 7)       # * = desempacotador
    # result: (1, 2, (3, 4, 5), {'x': 7})

# Example
def name(argumento_posicional, *pacote_de_argumentos):
    print(argumento_posicional, pacote_de_argumentos)

def name(argumento_nomead, **pacote_nomeado):
    print(argumento_posicional="I'm a named arg", pacote_nomeado)
