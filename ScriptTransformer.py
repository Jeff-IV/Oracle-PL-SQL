import json
import yaml

# Cargar archivo sqlnb (YAML)
with open("OraclePLSQLNotebook.sqlnb", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

cells = []

for cell in data["cells"]:
    content = cell["value"]

    if cell["kind"] == 1:  # Markdown
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": content
        })
    
    elif cell["kind"] == 2:  # Código
        cells.append({
            "cell_type": "code",
            "metadata": {},
            "source": content,
            "outputs": [],
            "execution_count": None
        })

notebook = {
    "cells": cells,
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 5
}

# Guardar como ipynb
with open("OraclePLSQL.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print("Convertido a archivo.ipynb")