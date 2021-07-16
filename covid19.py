
#! Ejercicio Covid 19

import requests as req
import os
import json
from covid19_2 import Statistics
import matplotlib.pyplot as plt
real_path = os.path.dirname(__file__)

# res = req.get(f'https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json').json()

# with open(f'{real_path}/covid.json', 'w', encoding = 'utf8') as file:
#     json.dump(res, file, ensure_ascii = False, indent = 4)

with open(f'{real_path}/covid.json', encoding = 'utf8') as file:
    data = json.load(file)['data']

#! Ejercicio 1

# resultado = list(filter(lambda mun: mun['fecha_informe'].split(' ')[0] == "2020/07/01", data))
# print(len(resultado))

#! Ejercicio 2

# resultado = list(filter(lambda mun: mun['fecha_informe'].split(' ')[0] == "2020/02/26", data))

# try:
#     resultado_2 = list(filter(lambda mun: mun['casos_confirmados_totales'] == True, resultado))
#     print(sum(resultado_2))
# except KeyError:
#     print('El número de casos confirmados a día 26/02/2020 es de 0')

#! Ejercicio 3

# resultado = filter(lambda mun: mun['fecha_informe'].split(' ')[0] == "2020/07/01", data)

# list_result = []
# for mun in resultado:
#     try:
#         list_result.append(mun['casos_confirmados_totales'])
#     except KeyError:
#         continue
# print(sum(list_result))

#! Ejercicio 4

# resultado = filter(lambda mun: mun['fecha_informe'].split(' ')[0] == "2020/07/01", data)

# list_result = []
# for mun in resultado:
#     try:
#         if mun['casos_confirmados_totales'] > 0:
#             list_result.append(mun)
#     except KeyError:
#         continue

# resultado_2 = sorted(list_result, key = lambda mun: mun['casos_confirmados_totales'], reverse = True)[0:10]


# [print(f'{mun["municipio_distrito"]}: {mun["casos_confirmados_totales"]}') for mun in resultado_2]

#! Ejercicio 5

dict_covid = {}
list_covid = []

for mun in data:
    if mun['fecha_informe'].split(' ')[0] not in list_covid:
        list_covid.append(mun['fecha_informe'].split(' ')[0])

for date in list_covid:
    resultado = filter(lambda mun: mun['fecha_informe'].split(' ')[0] == date, data)
    list_result = []
    for mun in resultado:
        try:
            list_result.append(mun['casos_confirmados_totales'])
        except KeyError:
            continue
    dict_covid[date] = sum(list_result)
    final_dict = dict(sorted(dict_covid.items(), key = lambda tupla: tupla[1]))
dates = list(final_dict.keys())
Y = list(final_dict.values())
X = [num for num in range(1, len(Y) + 1)]

#! Representación gráfica de la curva de casos totales de Covid

covid_data = Statistics(X, Y)
Y_until65 = Y[0:66]
X_until65 = [num for num in range(1, len(Y_until65) + 1)]

fig, ax = plt.subplots()
ax.plot(X_until65, Y_until65)
plt.ylabel('Casos de Covid')
plt.xlabel('Días de pandemia')
plt.show()

Y_after65 = Y[66:]
X_after65 = [num for num in range(1, len(Y_after65) + 1)]

after65 = Statistics(X_after65, Y_after65)
print(after65.rxy)

#! Ejercicio 17

print(after65.prediction(158))

fig, ax = plt.subplots()
ax.plot(X_after65, Y_after65)
plt.ylabel('Casos de Covid')
plt.xlabel('Días de pandemia')
plt.show()