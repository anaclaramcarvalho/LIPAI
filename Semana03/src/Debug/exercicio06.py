""" Crie um programa em Python que recebe como entrada o comprimento, altura e largura (em cm) de um aquário e calcule o volume,a potência,a quantidade de filtragem por hora."""

breakpoint()
aquario = {
    'comprimento': 23.5,
    'altura': 15.79,
    'largura': 8.5
}
def volume(aquario):
    v = (aquario['comprimento'] * aquario['altura'] * aquario['largura'] ) / 1000
    return v
v = volume(aquario)
print(v)

def potencia_termostato(temperatura_desejada, temperatura_ambiente, volume):
    potencia = volume * 0.05 * (temperatura_desejada - temperatura_ambiente)
    return potencia
p = potencia_termostato(35.7, 30.4, v)
print(p)

def filtragem(volume):
    filtro_min = 2 * volume
    filtro_max = 3 * volume
    return filtro_min, filtro_max

f = filtragem(v)
print(f)