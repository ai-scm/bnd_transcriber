# 🎙️ Blend Transcriptor — Instrucciones de Uso

Herramienta que convierte el audio de tus videos y grabaciones en texto escrito.  
Todo funciona en tu computador, **sin internet** y **sin límites de tamaño**.

---

## 📦 Prerrequisitos (solo la primera vez)

Antes de usar la herramienta necesitas instalar 3 cosas. Sigue cada enlace y las instrucciones:

---

### 1. Python (versión 3.9 o superior)

Python es el motor que hace funcionar la herramienta.

**Descarga:** [https://www.python.org/downloads/](https://www.python.org/downloads/)

**Instalación:**
1. Haz clic en el botón amarillo "Download Python 3.x.x"
2. Ejecuta el archivo descargado
3. ⚠️ **MUY IMPORTANTE:** Marca la casilla que dice **"Add Python to PATH"** antes de hacer clic en "Install Now"
4. Haz clic en "Install Now"
5. Espera a que termine y cierra el instalador

**Verificar que quedó bien instalado:**
1. Abre el menú de inicio y busca "cmd"
2. Escribe: `python --version`
3. Debe mostrar algo como: `Python 3.11.9`

---

### 2. FFmpeg

FFmpeg es lo que permite extraer el audio de los videos.

**Descarga:** [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

**Instalación rápida (recomendada):**
1. Abre el menú de inicio y busca "cmd"
2. Escribe el siguiente comando y presiona Enter:
   ```
   winget install Gyan.FFmpeg
   ```
3. Espera a que termine la instalación

**Instalación manual (si winget no funciona):**
1. Ve a [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
2. En la sección "release builds", descarga el archivo `ffmpeg-release-full.7z`
3. Extrae el contenido en una carpeta (por ejemplo `C:\ffmpeg`)
4. Pide ayuda al equipo técnico para agregarlo al PATH del sistema

---

### 3. Dependencias de Python (librerías)

Son componentes adicionales que la herramienta necesita para funcionar.

**Instalación:**
1. Abre el menú de inicio y busca "cmd"
2. Escribe estos comandos uno por uno (presiona Enter después de cada uno):
   ```
   cd C:\Users\Juan Tinjaca\Documents\Repos\bnd_transcriber\transcriber
   pip install -r requirements.txt
   ```
3. Espera a que se descarguen e instalen todos los paquetes (puede tardar varios minutos)

> 💡 Esto solo se hace una vez. No necesitas repetirlo cada vez que uses la herramienta.

---

## 🚀 Cómo usar la herramienta

### Paso 1 — Coloca tu archivo

Copia el video (`.mp4`) o audio (`.mp3`) que quieres transcribir en esta carpeta:

```
📁 transcriber → 📁 Videos
```

> Puedes arrastrar el archivo directamente desde el explorador de Windows.

---

### Paso 2 — Ejecuta la herramienta

Haz **doble clic** en el archivo:

```
📄 iniciar_transcriptor.bat
```

Se abrirá una ventana negra que dice "Blend Transcriptor". Espera a que diga **"La herramienta está lista!"** y se abrirá tu navegador automáticamente.

> ⚠️ **No cierres la ventana negra.** Si la cierras, la herramienta se apaga.

---

### Paso 3 — Transcribe

En el navegador verás la interfaz de Blend:

1. **Selecciona** tu archivo del menú desplegable
2. Haz clic en **"Transcribir"**
3. Espera a que la barra de progreso llegue al 100%

---

### Paso 4 — Obtén el resultado

Cuando termine tienes 3 formas de obtener el texto:

| Opción | Cómo |
|--------|------|
| 📋 **Copiar** | Haz clic en "Copiar texto" y pégalo donde quieras (Word, correo, etc.) |
| ⬇️ **Descargar** | Haz clic en "Descargar .txt" para guardar un archivo de texto |
| 📁 **Carpeta** | El texto se guarda automáticamente en `transcriber/transcripciones/` |

---

### Paso 5 — Cerrar la herramienta

Cuando termines, simplemente **cierra la ventana negra** (la X de la esquina) o presiona cualquier tecla en ella.

---

## ⏱️ ¿Cuánto tarda?

| Duración del archivo | Tiempo aproximado |
|---------------------|-------------------|
| 5 minutos | 2 – 10 minutos |
| 30 minutos | 15 – 60 minutos |
| 1 hora | 30 min – 2 horas |
| 2+ horas | 1 – 4+ horas |

> Los tiempos dependen de la potencia de tu computador. Si tienes tarjeta gráfica NVIDIA, será mucho más rápido.

---

## 🎯 Tips para mejores resultados

- ✅ **Audio claro** sin mucho ruido de fondo
- ✅ **Un hablante a la vez** (no varias personas hablando encima)
- ✅ **Micrófono cerca** del hablante
- ✅ **Archivos más cortos** se procesan más rápido
- ❌ Evita grabaciones con música de fondo fuerte
- ❌ Evita audios con mucho eco o reverberación

---

## ❓ Solución de problemas

### "Al hacer doble clic no pasa nada"
→ Haz clic derecho sobre `iniciar_transcriptor.bat` → "Ejecutar como administrador"

### "Dice que Python no está instalado"
→ Instala Python siguiendo las instrucciones de la sección de Prerrequisitos. **No olvides marcar "Add to PATH".**

### "El navegador se abre pero dice que no puede conectar"
→ Espera un poco más. La primera vez que se ejecuta, el modelo de inteligencia artificial se descarga y eso puede tardar unos minutos. Recarga la página (F5) después de un momento.

### "No veo mi archivo en la lista"
→ Verifica que:
  - El archivo esté en la carpeta `transcriber/Videos/`
  - El archivo sea `.mp4` o `.mp3`
  - Recarga la página (F5)

### "La transcripción tiene errores"
→ Es normal. La herramienta hace su mejor esfuerzo pero puede confundir palabras, especialmente con:
  - Ruido de fondo
  - Varios hablantes simultáneos
  - Términos técnicos o nombres propios
  - Audio de baja calidad

Revisa y corrige manualmente lo que sea necesario.

### "Se quedó trabado en un porcentaje"
→ No te preocupes, archivos largos pueden parecer trabados pero siguen procesándose. Dale tiempo. Si después de 30 minutos no avanza, cierra todo y vuelve a intentar.

### Otro error no listado aquí
→ Toma una **captura de pantalla** del error y envíala al equipo técnico.

---

## 📁 Estructura de carpetas

```
📁 bnd_transcriber/
│
├── 📄 iniciar_transcriptor.bat    ← DOBLE CLIC AQUÍ PARA INICIAR
├── 📄 INSTRUCCIONES.md            ← Este archivo
│
└── 📁 transcriber/
    ├── 📁 Videos/                 ← PON TUS ARCHIVOS AQUÍ
    ├── 📁 transcripciones/        ← AQUÍ SE GUARDAN LOS RESULTADOS
    └── 🐍 app.py                  ← (no tocar)
```

---

## 📞 Soporte

Si algo no funciona como se describe aquí, contacta al equipo técnico con:
- Captura de pantalla del error
- Nombre del archivo que intentabas transcribir
- Qué paso estabas siguiendo cuando falló

---

> **Versión:** 1.0 · Mayo 2026  
> **Motor:** OpenAI Whisper (medium) · Flask
