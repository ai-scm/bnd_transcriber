<div align="center">

<br/>

```
██████╗ ██╗     ███████╗███╗   ██╗██████╗
██╔══██╗██║     ██╔════╝████╗  ██║██╔══██╗
██████╔╝██║     █████╗  ██╔██╗ ██║██║  ██║
██╔══██╗██║     ██╔══╝  ██║╚██╗██║██║  ██║
██████╔╝███████╗███████╗██║ ╚████║██████╔╝
╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝
```

### ◈ Transcriptor de Video ◈

**Convierte el audio de tus videos `.mp4` en texto — 100% local, sin APIs, sin límites.**

<br/>

![Python](https://img.shields.io/badge/Python-3.9+-1DF5F4?style=for-the-badge&logo=python&logoColor=black)
![Flask](https://img.shields.io/badge/Flask-3.x-1DF5F4?style=for-the-badge&logo=flask&logoColor=black)
![Whisper](https://img.shields.io/badge/OpenAI_Whisper-base-1DF5F4?style=for-the-badge&logo=openai&logoColor=black)
![License](https://img.shields.io/badge/Uso-Interno-1a3a5c?style=for-the-badge)

<br/>

</div>

---

## ◈ ¿Qué hace?

Herramienta web interna que transcribe automáticamente el audio de archivos `.mp4` usando **OpenAI Whisper** de forma completamente local. Sin API keys, sin internet, sin límite de tamaño de archivo.

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   📁 Videos/mi_video.mp4                               │
│          │                                              │
│          ▼                                              │
│   🎙️  Whisper extrae y transcribe el audio             │
│          │                                              │
│          ▼                                              │
│   📄 transcripciones/mi_video.txt  ✦  UI en vivo      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## ◈ Estructura del proyecto

```
Transcriptions/
│
├── 📁 Videos/                    ← Coloca aquí tus .mp4
│
├── 📁 transcriber/
│   ├── 🐍 app.py                 ← Servidor Flask + lógica Whisper
│   ├── 📄 requirements.txt       ← Dependencias Python
│   ├── 📄 README.md              ← Este archivo
│   │
│   ├── 📁 templates/
│   │   └── 🌐 index.html         ← Interfaz web
│   │
│   └── 📁 transcripciones/       ← Salida automática (se crea sola)
│
└── 📄 .gitignore
```

---

## ◈ Requisitos

### Python 3.9+
```bash
python --version
```

### ffmpeg
```bash
# Windows
winget install ffmpeg
```

> Si ffmpeg no queda en el PATH, configura la ruta directamente en `app.py` (ver sección de configuración).

### Dependencias Python
```bash
cd transcriber
pip install -r requirements.txt
```

| Paquete | Versión | Uso |
|---|---|---|
| `flask` | 3.x | Servidor web |
| `openai-whisper` | latest | Motor de transcripción |
| `ffmpeg-python` | latest | Extracción de audio |

---

## ◈ Configuración

### 🔧 Ruta de ffmpeg — `app.py` línea 8

Si ffmpeg no está en el PATH del sistema, se configura manualmente:

```python
FFMPEG_BIN = r"C:\Users\<usuario>\AppData\Local\Microsoft\WinGet\Packages\...\bin"
```

Para encontrar la ruta exacta en Windows:
```powershell
Get-ChildItem -Path "$env:LOCALAPPDATA" -Recurse -Filter "ffmpeg.exe" -ErrorAction SilentlyContinue | Select-Object FullName
```

---

### 🧠 Modelo de Whisper — `app.py` línea 22

```python
model = whisper.load_model("base")  # ← cambia aquí
```

```
┌──────────┬──────────────┬───────────┬────────────────┐
│  Modelo  │  Velocidad   │ Precisión │  VRAM mínima   │
├──────────┼──────────────┼───────────┼────────────────┤
│  tiny    │  ⚡ Muy rápido│    ★☆☆☆  │    ~1 GB       │
│  base    │  🚀 Rápido   │    ★★☆☆  │    ~1 GB  ✅   │
│  small   │  🔄 Moderado │    ★★★☆  │    ~2 GB       │
│  medium  │  🐢 Lento    │    ★★★★  │    ~5 GB       │
│  large   │  🐌 Muy lento│    ★★★★★ │   ~10 GB       │
└──────────┴──────────────┴───────────┴────────────────┘
```

> ✅ `base` es el balance recomendado para uso en CPU.

---

## ◈ Uso

### 1 — Agrega tus videos

```
Transcriptions/
└── Videos/
    ├── reunion_enero.mp4
    ├── presentacion_q1.mp4
    └── entrevista.mp4
```

### 2 — Inicia el servidor

```bash
cd transcriber
python app.py
```

```
 * Running on http://127.0.0.1:5000
 * Threaded mode enabled
```

### 3 — Abre la interfaz

```
http://localhost:5000
```

### 4 — Transcribe

```
[ Selecciona un video ▾ ]

[ ████████████████████░░░░  78% ]
  Procesando segmento 42 de 54...

  Carga ✦  Análisis ✦  Transcripción ●  Guardado
```

---

## ◈ API Reference

### `GET /videos`
Lista todos los `.mp4` disponibles en la carpeta `Videos/`.

```json
{
  "videos": ["reunion_enero.mp4", "presentacion_q1.mp4"]
}
```

---

### `POST /transcribe`
Inicia la transcripción de un video. Devuelve un `job_id` para seguir el progreso.

**Request:**
```json
{ "filename": "reunion_enero.mp4" }
```

**Response:**
```json
{ "job_id": "reunion_enero.mp4_1743000000" }
```

---

### `GET /progress/<job_id>`
**Server-Sent Events** — emite el progreso en tiempo real hasta completar.

```
data: {"status": "processing", "progress": 45, "message": "Procesando segmento 12 de 27..."}
data: {"status": "done", "progress": 100, "transcript": "...", "language": "es", "file_size_gb": 1.2}
```

| `status` | Descripción |
|---|---|
| `queued` | En cola, esperando inicio |
| `loading` | Cargando el archivo de audio |
| `processing` | Transcribiendo segmentos |
| `saving` | Guardando el archivo `.txt` |
| `done` | Completado exitosamente |
| `error` | Error durante el proceso |

---

## ◈ Salida

Cada transcripción se guarda automáticamente en:

```
transcriber/transcripciones/<nombre_del_video>.txt
```

**Ejemplo:**
```
Videos/reunion_enero.mp4  →  transcripciones/reunion_enero.txt
```

Desde la UI también puedes:
- `📋` Copiar el texto al portapapeles
- `⬇️` Descargar el `.txt` directamente

---

## ◈ Rendimiento

```
┌─────────────────────────────────────────────────────────┐
│  CPU (sin GPU)                                          │
│  Tiempo ≈ 1x – 4x la duración del video                │
│  Ej: video de 1h  →  entre 1h y 4h de procesamiento    │
│                                                         │
│  GPU NVIDIA (CUDA)                                      │
│  Whisper la detecta automáticamente                     │
│  Tiempo ≈ 10x – 20x más rápido que CPU                 │
└─────────────────────────────────────────────────────────┘
```

> El warning `FP16 is not supported on CPU` es **normal** cuando no hay GPU. El proceso continúa en FP32 sin ningún problema.

---

## ◈ Solución de problemas

| ❌ Error | 🔍 Causa | ✅ Solución |
|---|---|---|
| `[WinError 2] archivo no encontrado` | ffmpeg no está en el PATH | Configura `FFMPEG_BIN` en `app.py` con la ruta absoluta |
| `No hay videos en la carpeta Videos/` | Carpeta vacía o ruta incorrecta | Verifica que los `.mp4` estén en `Transcriptions/Videos/` |
| `FP16 is not supported on CPU` | Sin GPU disponible | Warning inofensivo, el proceso continúa normalmente |
| Transcripción muy lenta | Modelo grande en CPU | Cambia a `tiny` o `base` en `app.py` |
| Puerto 5000 ocupado | Otro proceso usa el puerto | Cambia: `app.run(port=5001)` en `app.py` |

---

<div align="center">

<br/>

`Powered by OpenAI Whisper` &nbsp;·&nbsp; `Flask` &nbsp;·&nbsp; `Blend`

<br/>

</div>
