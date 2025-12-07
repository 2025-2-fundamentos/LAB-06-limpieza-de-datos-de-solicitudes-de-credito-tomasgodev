"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import os
import pandas as pd

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    
    input_path = "files/input/solicitudes_de_credito.csv"
    output_dir = "files/output"
    output_path = os.path.join(output_dir, "solicitudes_de_credito.csv")

    df = pd.read_csv(input_path, sep=";", index_col=0)


    # sexo: solo a minúsculas
    df["sexo"] = df["sexo"].str.lower()

    df["tipo_de_emprendimiento"] = (
        df["tipo_de_emprendimiento"]
        .str.lower()
        .str.strip()
    )

    df["idea_negocio"] = (
        df["idea_negocio"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
        .str.strip()
    )

    df["barrio"] = (
        df["barrio"]
        .str.lower()
        .str.replace("-", " ", regex=False)
        .str.replace("_", " ", regex=False)
    )

    df["línea_credito"] = (
        df["línea_credito"]
        .str.lower()
        .str.strip()
        .str.replace("-", " ", regex=False)
        .str.replace("_", " ", regex=False)
        .str.strip()
    )

    fecha_1 = pd.to_datetime(
        df["fecha_de_beneficio"],
        format="%d/%m/%Y",
        errors="coerce",
    )
    fecha_2 = pd.to_datetime(
        df["fecha_de_beneficio"],
        format="%Y/%m/%d",
        errors="coerce",
    )
    df["fecha_de_beneficio"] = fecha_1.combine_first(fecha_2)


    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .str.strip()
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace(".00", "", regex=False)
    )
    df["monto_del_credito"] = pd.to_numeric(
        df["monto_del_credito"], errors="coerce"
    )

    df = df.drop_duplicates()
    df = df.dropna()

    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(output_path, sep=";", index=False)