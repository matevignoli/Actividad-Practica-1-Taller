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