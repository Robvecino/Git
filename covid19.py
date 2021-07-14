
#! Ejercicio Covid 19

import requests as req
import os
import json
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
    final = sorted(dict_covid.items())
[print(f'{tupla[0]}: {tupla[1]}') for tupla in final]

