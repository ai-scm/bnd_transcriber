@echo off
title Blend Transcriptor
echo.
echo  ============================================
echo       Blend - Transcriptor de Audio ^& Video
echo  ============================================
echo.
echo  Iniciando la herramienta...
echo  (No cierres esta ventana mientras la uses)
echo.

cd /d "%~dp0transcriber"

:: Verificar que Python existe
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo  [ERROR] Python no esta instalado o no esta en el PATH.
    echo  Contacta al equipo tecnico.
    echo.
    pause
    exit /b 1
)

echo  Cargando el modelo de transcripcion (esto puede tardar unos segundos)...
echo.

:: Iniciar el servidor en segundo plano
start /b python app.py

:: Esperar a que el servidor este listo (intentar conectar cada 2 segundos)
:wait_loop
timeout /t 2 /nobreak >nul
curl -s -o nul http://localhost:5000 >nul 2>&1
if %errorlevel% neq 0 (
    echo  Esperando a que el servidor este listo...
    goto wait_loop
)

echo.
echo  -----------------------------------------------
echo   La herramienta esta lista!
echo   Abriendo el navegador...
echo  -----------------------------------------------
echo.

:: Ahora si abrir el navegador
start "" http://localhost:5000

echo  Si el navegador no se abrio, ve manualmente a:
echo  http://localhost:5000
echo.
echo  Para cerrar la herramienta, cierra esta ventana.
echo.

:: Mantener la ventana abierta (si se cierra, mata el servidor)
pause >nul
