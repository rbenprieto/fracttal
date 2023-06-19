import pandas as pd
from datetime import datetime


def read_csv():
    """
    Util function for read the csv file, filter data and return results
    """

    # Se lee el archivo y limito las columnas de estudio del df
    df = pd.read_csv("apps/prueba_tecnica/sensor.csv")
    df = df[["timestamp", "sensor_07", "sensor_47", "machine_status"]]

    # Inicia limpieza de datos
    # Convierto la columna timestamp a formato datetime, lo que no pueda convertir lo pone nulo
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Elimina los valores nulos que existan en la columna timestamp. Así me aseguro que filtraré sobre fechas, evitando excepciones
    df.dropna(subset=["timestamp"])

    # Hago el filtro en el año 2018 y el mes de abril
    df = df[(df["timestamp"].dt.year == 2018) & (df["timestamp"].dt.month == 4)]

    # Filtro entre los valores determinados el el sensor 07 Ó 47, importante mencionar que no se especificó que ambos sensores debían cumplir esta condición
    df = df[
        (df["sensor_07"] > 20) & (df["sensor_07"] < 30)
        | (df["sensor_47"] > 20) & (df["sensor_47"] < 30)
    ]

    # Asigno una columna que se llama id y es consecutiva para saber cuantos registros cumplen con la condición
    df["id"] = range(1, len(df) + 1)

    # Organizo las columnas en orden
    df = df.reindex(
        columns=["id", "timestamp", "machine_status", "sensor_07", "sensor_47"]
    )

    list_measurements_json = format_data(df)

    # Devuelvo la información en formato json
    return list_measurements_json


def format_data(data):
    """Inicio la estructura para devolver la información

    Quiero validar que cuando el df tenga en un mismo registro, valores válidos en el sensor 07 y 47, se marquen como registros separados.
    Cada valor válido, debe ser mostrado de forma independiente, mejora la comprensión.
    """

    df = data

    # Hago una lista vacía para despúes appendear y un for para verificar registro por registro los valores
    list_measurements = []
    for index, row in df.iterrows():
        # Si ambos sensores cumplen con las condiciones de valores en un mismo registro, se generan dos registros, uno para el primer sensor y otro para el segundo
        if (row["sensor_07"] >= 20 and row["sensor_07"] <= 30) and (
            row["sensor_47"] >= 20 and row["sensor_47"] <= 30
        ):
            new_row_1 = row.copy()
            new_row_1["sensor_47"] = None
            new_row_2 = row.copy()
            new_row_2["sensor_07"] = None

            list_measurements.append(new_row_1)
            list_measurements.append(new_row_2)

        # Si solo el sensor 07 cumple entonces el valor del sensor 47 se pone nulo, ya que ese valor no califica para el análisis
        elif row["sensor_07"] >= 20 and row["sensor_07"] <= 30:
            row["sensor_47"] = None
            list_measurements.append(row)

        # Si solo el sensor 47 cumple entonces el valor del sensor 07 se pone nulo, ya que ese valor no califica para el análisis
        elif row["sensor_47"] >= 20 and row["sensor_47"] <= 30:
            row["sensor_07"] = None
            list_measurements.append(row)

    # Convertir la lista de mediciones en un nuevo DataFrame
    new_df = pd.DataFrame(list_measurements)

    # Ahora construyo un json en una lista vacía mediante un for, creando un objeto y appendeando, terminando de procesar la información
    list_measurements_json = []
    for index, row in new_df.iterrows():
        register_json = {
            "id": row["id"],
            "fecha": row["timestamp"],
            "machine_status": row["machine_status"],
            # Para mí es importante mostrar el nombre del sensor que aplica y el valor que obtuvo, por esto hago un ternario para evaluar que valor poner
            "sensor": "sensor_07" if pd.notnull(row["sensor_07"]) else "sensor_47",
            "valor_medicion": row["sensor_07"]
            if pd.notnull(row["sensor_07"])
            else row["sensor_47"],
        }
        list_measurements_json.append(register_json)

    return list_measurements_json


def processing_data(data):
    records = []
    for item in data:
        # Obtener los valores de la fecha, hora y estado
        timestamp_str = item['fecha']
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        date = timestamp.date().strftime('%Y-%m-%d')
        time = timestamp.time().strftime('%H:%M:%S')

        if 20 < item["medicion"] < 30:
            record = {
                'fecha': date,
                'hora': time,
                'sensor': item["sensor"],
                'medicion': item["medicion"],
                'estado': item['estado']
            }
            records.append(record)

    df = pd.DataFrame(records)
    return df


def data_for_saving(data):
    list_data = []
    for index, row in data.iterrows():
        fecha = datetime.strptime(row["fecha"], "%Y-%m-%d").date()
        hora = datetime.strptime(row["hora"], "%H:%M:%S").time()
        dict = {
            "fecha": datetime.combine(fecha, hora),
            "sensor": row["sensor"],
            "valor_medicion": row["medicion"],
            "machine_status": row["estado"],
        }
        list_data.append(dict)
        
    return list_data