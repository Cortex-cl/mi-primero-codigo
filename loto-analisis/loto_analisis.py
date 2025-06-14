import pandas as pd
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
from collections import Counter
from datetime import datetime

archivo_excel = 'Loto/loto_2025.xlsx'
df = pd.read_excel(archivo_excel)
df.columns = df.columns.str.strip()


#funcion para convertir fecha 

def convertir_fecha(fecha_str):
    try:
        return datetime.strptime(fecha_str, "%a %d %b %Y")
    except:
        return pd.NaT

df['Fecha'] = df['Fecha'].apply(convertir_fecha)

df = df.dropna(subset=['Fecha'])


df['Mes'] = df['Fecha'].dt. strftime('%B')
df['Año'] = df['Fecha'].dt.year


#funcion para extraer los 6 números
def extraer_numeros(numeros_str):
    numeros = [int(n) for n in numeros_str.strip().split(',') if n.strip()]
    return numeros [:6]

df['Números_Lista'] = df['Números'].apply(extraer_numeros)

grupos = df.groupby(['Año', 'Mes'])

for (anio, mes), grupo in sorted(grupos):
    todos_los_numeros = []
    todos_comodines = []
    todos_multiplicadores = []

    for _, fila in grupo.iterrows():
        todos_los_numeros.extend(fila['Números_Lista'])
        todos_comodines.append(int(fila['Comodín']))
        todos_multiplicadores.append(int(fila['Multiplicador']))

    contador_numeros = Counter(todos_los_numeros)
    contador_comodines = Counter(todos_comodines)
    contador_multiplicadores = Counter(todos_multiplicadores)

    print(f"\n {mes.upper()} {anio}")
    print ("-" * 30)

    print("Números más frecuentes:")
    for num, freq in contador_numeros.most_common():
        print(f" Número {num}: {freq} veces")
    
    print("\n Comodines más frecuentes:")
    for num, freq in contador_comodines.most_common():
        print(f" Comodín {num}: {freq} veces")
    
    print("\n Multiplicadores más frecuentes:")
    for num, freq in contador_multiplicadores.most_common():
        print(f" Multiplicador {num}: {freq} veces")