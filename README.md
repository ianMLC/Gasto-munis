# Uso

Requiere Python 3.10 o superior.

1. Crear el entorno virtual e instalar las dependencias:

```bash
   python3 -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
```
2. Estructura
```bash
Gasto-munis/
├── data/
│   ├── raw/              # descargas de SINIM tal cual (no se versiona)
│   └── processed/        # datos limpios en formato ancho
├── docs/
│   └── diccionario_variables.md   # las tablas de códigos que armaste
├── notebooks/
│   ├── 01_descarga.ipynb
│   ├── 02_limpieza.ipynb
│   └── 03_analisis.ipynb
├── reports/
│   └── figures/
├── src/
│   ├── config.py         # comunas, años y códigos de variables
│   └── sinim.py          # funciones de descarga y transformación
├── .gitignore
├── README.md
└── requirements.txt
```

3. Abrir los notebooks:

```bash
   jupyter lab
```


## Limitaciones de los datos

- `pct_poblacion_rural` no tiene datos para 2015-2017 en SINIM.
- `viviendas` no tiene datos para 2015-2021 en SINIM.
- Ambas variables provienen probablemente de datos censales. No se imputaron valores.