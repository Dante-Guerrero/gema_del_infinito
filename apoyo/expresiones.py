import string

def listAlphabet():
  return list(string.ascii_lowercase)

letras = listAlphabet()

articulos = [
    'el',
    'la',
    'lo',
    'los',
    'las',
    'un',
    'una',
    'unos',
    'unas'
]

pronombres =[
    'esto',
    'este',
    'esa',
    'ese',
    'ello',
    'al',
    'su',
    'sus',
    'le',
    'ésta',
    'al'
]

otros = [
    'para',
    'tal',
    'sea',
    'mismo',
    'misma',
    'dado',
    'nro',
    'siguiente',
    'todas',
    'de',
    'en',
    'por',
    'del',
    'con',
    'dicha',
    'dicho',
    'sin',
    'se',
    'sobre',
    'cual',
    'si',
    'ya',
    'así',
    'casi',
    'no',
    'que',
    'ni',
    'como',
    'muy',
    'demás',
    'más',
    'cada',
    'ya',
    'cual',
    'desde'
]

expresiones_excluidas = letras + articulos + pronombres + otros
