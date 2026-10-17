from pathlib import Path


PATH = Path(__file__).resolve().parent.parent
DATA_RAW = PATH / "data" / "raw"
DATA_PROCESSED = PATH / "data" / "processed"


COMMUNES = {
    "08110" : "Talcahuano",
    ## completar despues a gusto
}

YEARS = list(range(2015,2026))

#diccionario de terminos
GROUPS = {
    "presupuesto": {
        "4210": "ppto_inicial_ingresos",
        "4211": "ppto_inicial_gastos",
        "4212": "ppto_vigente_ingresos",
        "4213": "ppto_vigente_gastos",
        "1093": "gasto_devengado",
        "4441": "ppto_inicial_saldo_caja",
        "4226": "ppto_vigente_saldo_caja",
    },
    "ingresos": {
        "910": "aporte_al_fcm",
        "1110": "ingreso_total",
        "4245": "ingreso_total_sin_saldo_caja",
        "879": "ingresos_propios_permanentes",
        "880": "ingresos_fcm",
        "4251": "ing_impuesto_territorial",
        "4173": "ing_patentes",
        "4174": "ing_permisos_circulacion",
        "3954": "ing_derechos_aseo",
        "883": "ing_transferencias",
        "3883": "ing_pmu",
        "3893": "ing_pmb",
    },
    "gastos_areas": {
        "4162": "area_gestion_interna",
        "4163": "area_servicios_comunitarios",
        "4164": "area_actividades_municipales",
        "4165": "area_programas_sociales",
        "4166": "area_programas_recreacionales",
        "4167": "area_programas_culturales",
    },
    "personal": {
        "1305": "pers_planta",
        "1306": "pers_contrata",
        "4421": "pers_honorarios",
        "4422": "pers_codigo_trabajo",
        "3964": "pers_programas_comunitarios",
    },
    "servicios": {
        "3923": "serv_aseo_total",
        "3925": "serv_alumbrado_publico",
        "4040": "serv_jardines_total",
        "3921": "serv_electricidad_total",
        "3922": "serv_agua_total",
    },
    "transferencias": {
        "1302": "transf_educacion",
        "1301": "transf_salud",
        "3783": "transf_org_comunitarias",
        "3784": "transf_asistencia_social",
        "1103": "inversion_municipal",
    },
    "indicadores": {
        "4243": "pct_ejecucion_sinim",
        "1086": "pct_ipp_ingreso_total",
        "1087": "pct_fcm_ingreso_total",
        "1272": "pct_dependencia_fcm",
        "1109": "pct_aporte_vs_recepcion_fcm",
        "1094": "pct_gasto_corriente",
        "1095": "pct_inversion",
        "4237": "pct_area_gestion_interna",
        "1310": "pct_eficiencia_patentes",
    },
    "contexto": {
        "571": "poblacion",
        "827": "densidad_poblacion",
        "835": "pct_poblacion_rural",
        "4613": "viviendas",
    },
    "gastos_subtitulos": {
    "894": "gasto_corriente",
    "3975": "sub21_personal",
    "3770": "sub22_bienes_servicios",
    "1229": "sub24_transferencias_corrientes",
    },
}