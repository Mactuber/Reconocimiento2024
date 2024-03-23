#!/bin/bash

# Crear los directorios
mkdir -p nmap scripts exploits content tmp info creds

# Verificar si se crearon correctamente
if [ $? -eq 0 ]; then
    echo "Los directorios se han creado correctamente."
else
    echo "Hubo un error al crear los directorios."
    exit 1
fi

# Mostrar la estructura de directorios
echo "Estructura de directorios creada:"
ls -l
