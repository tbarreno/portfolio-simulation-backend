#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Ajusta los datos
#

import os
import pandas as pd

# Directorio base
data_dir = "/home/sp82186/devel/data"

# Año de inicio y de final
year_start = 2013
year_end = 2018

# Directorios de entrada y de salida
input_dir = os.path.join(data_dir, "symbols-orig")
output_dir = os.path.join(data_dir, "symbols")

# Bucle de fichero
input_files = os.listdir(input_dir)

for file in input_files:

    # Comprobamos el formato del fichero (sólo los '*_data.csv')
    if not file.endswith("_data.csv"):
        print(f" - Ignored: {file}")
        continue

    # Ruta completa a los ficheros
    input_file = os.path.join(input_dir, file)
    output_file = os.path.join(output_dir, file)

    # Procesamos el fichero
    print(f" * {input_file} -> {output_file}")

    # Cargamos el fichero
    dt = pd.read_csv(input_file)
    new_dt = pd.DataFrame(columns=dt.columns)

    # Bucle por años y meses
    for year in range(year_start, year_end + 1):
        for month in range(1, 13):
            # Montamos la cadena de texto de la fecha
            date_str = f"{year}-{month:02}"

            # Obtenemos las líneas de ese mes
            month_data = dt[dt["date"].str.startswith(date_str)]

            # Si no hay datos para ese año-mes, pasamos al siguiente
            if month_data.shape[0] == 0:
                continue

            # Generamos la línea de datos
            open = month_data.iloc[0].open
            close = month_data.iloc[-1].close
            high = month_data["high"].max()
            low = month_data["low"].min()
            volume = month_data["volume"].sum()
            name = month_data.iloc[0].Name

            new_dt = new_dt.append({
                "date": date_str,
                "open": open,
                "high": high,
                "low": low,
                "close": close,
                "volume": volume,
                "Name": name
            }, ignore_index=True)

    # Escribimos el fichero
    new_dt.to_csv(output_file)
