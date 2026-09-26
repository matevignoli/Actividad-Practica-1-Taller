columnas = {
    "PONDERA": {"tipo": "int", "completitud": 100},
    "ESTADO": {"tipo": "int", "completitud": 95},
    "CAT_OCUP": {"tipo": "int", "completitud": 80},
    "EDAD": {"tipo": "int", "completitud": 99},
    "REGION": {"tipo": "int", "completitud": 100},
    "AGLOMERADO": {"tipo": "int", "completitud": 100},
    "ANO4": {"tipo": "int", "completitud": 100},
    "TRIMESTRE": {"tipo": "int", "completitud": 100},
    "ITF": {"tipo": "int", "completitud": 60},
    "MAS_500": {"tipo": "str", "completitud": 100},
    "GDECCFR": {"tipo": "int", "completitud": 55}
}

# 

roles = {
    "docente": {
        "columnas": ["EDAD", "ESTADO", "REGION", "AGLOMERADO"],
        "criterio": "nombre",
        "orden": "A"
    },
    "investigador": {
        "columnas": ["PONDERA", "ESTADO", "CAT_OCUP", "ITF", "GDECCFR"],
        "criterio": "completitud",
        "orden": "B",
        "umbral": 80
    },
    "analista": {
        "columnas": ["REGION", "AGLOMERADO", "MAS_500", "ANO4", "TRIMESTRE"],
        "criterio": "completitud",
        "orden": "A"
    }
}
 
# 

def generar_informe(columnas, config_roles, rol=None):
    """
    genera un informe con las columnas correspondientes según el rol solicitado,
    aplicando filtros de completitud y criterios de ordenamiento.
    si no se especifica rol, devuelve todas las columnas ordenadas por completitud descendente.
    """
    # Condición por defecto: si no se especifica un rol
    if rol is None:
        todas_las_columnas = list(columnas.keys())
        return sorted(todas_las_columnas, key=lambda col: columnas[col]["completitud"], reverse=True)

    if rol not in config_roles:
        return "El rol solicitado no existe."

    config = config_roles[rol]
    columnas_interes = config["columnas"]
    criterio = config["criterio"]
    orden_descendente = config["orden"] == "B"
    umbral_minimo = config.get("umbral", 0)

    nombres_filtrados = list(filter( lambda col: columnas[col]["completitud"] >= umbral_minimo, columnas_interes))

    informe_detallado = [(col, columnas[col]) for col in nombres_filtrados]

    if criterio == "nombre":
        return sorted(informe_detallado, key=lambda elem: elem[0], reverse=orden_descendente)
    else:
        return sorted(informe_detallado, key=lambda elem: elem[1]["completitud"], reverse=orden_descendente)

# Bloque de pruebas
if __name__ == "__main__":
    print("--- DOCENTE (Alfabético Ascendente, sin umbral) ---")
    for col in generar_informe(columnas, roles, "docente"): print(col)
    
    print("\n--- INVESTIGADOR (Completitud Descendente, Umbral 80) ---")
    for col in generar_informe(columnas, roles, "investigador"): print(col)

    print("--- ANALISTA (Completitud Ascendente, sin umbral) ---")
    for col in generar_informe(columnas, roles, "analista"): print(col)
    

 