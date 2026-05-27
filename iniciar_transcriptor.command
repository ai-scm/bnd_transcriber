#!/bin/bash

echo ""
echo "  ============================================"
echo "       Blend - Transcriptor de Audio & Video"
echo "  ============================================"
echo ""
echo "  Iniciando la herramienta..."
echo "  (No cierres esta ventana mientras la uses)"
echo ""

# Navegar a la carpeta del proyecto
cd "$(dirname "$0")/transcriber"

# Verificar que Python3 existe
if ! command -v python3 &> /dev/null; then
    echo "  [ERROR] Python3 no esta instalado."
    echo "  Instala con: brew install python"
    echo ""
    read -p "  Presiona Enter para cerrar..."
    exit 1
fi

# Verificar que ffmpeg existe
if ! command -v ffmpeg &> /dev/null; then
    echo "  [ERROR] ffmpeg no esta instalado."
    echo "  Instala con: brew install ffmpeg"
    echo ""
    read -p "  Presiona Enter para cerrar..."
    exit 1
fi

echo "  Cargando el modelo de transcripcion (esto puede tardar unos segundos)..."
echo ""

# Iniciar el servidor en segundo plano
python3 app.py &
SERVER_PID=$!

# Esperar a que el servidor este listo
echo "  Esperando a que el servidor este listo..."
until curl -s -o /dev/null http://localhost:5000 2>/dev/null; do
    sleep 2
    echo "  Esperando..."
done

echo ""
echo "  -----------------------------------------------"
echo "   La herramienta esta lista!"
echo "   Abriendo el navegador..."
echo "  -----------------------------------------------"
echo ""

# Abrir el navegador
open http://localhost:5000

echo "  Si el navegador no se abrio, ve manualmente a:"
echo "  http://localhost:5000"
echo ""
echo "  Para cerrar la herramienta, cierra esta ventana"
echo "  o presiona Ctrl+C."
echo ""

# Esperar a que el usuario cierre
wait $SERVER_PID
