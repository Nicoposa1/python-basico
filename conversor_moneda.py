pesos = int(input('¿Cuántos pesos tenés?: '))
pesos = float(pesos)
valor_dolar_blue = 145
dolares = pesos / valor_dolar_blue
dolares = round(dolares, 2)
dolares = str(dolares)
print('Tenés $' + dolares + ' dólares blue')

dolar = int(input('¿Cuantos dólares tenés?: '))
dolar = float(dolar)
valor_pesos = 0.011
pesos_argentino = dolar/valor_pesos
pesos_argentino = round(pesos_argentino, 2)
pesos_argentino = str(pesos_argentino)
print('Tenés $' + pesos_argentino + ' pesos argentinos')
