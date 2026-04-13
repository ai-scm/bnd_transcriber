# Blend — Transcriptor de Video

Herramienta web interna para transcribir automáticamente el audio de archivos `.mp4` usando [OpenAI Whisper](https://github.com/openai/whisper) de forma local, sin necesidad de API keys ni conexión a internet.

---

## Estructura del proyecto

```
Transcriptions/
├── Videos/                  # Carpeta donde se colocan los .mp4 a transcribir
├── transcriber/
│   ├── app.py               # Servidor Flask (backend)
│   ├── requirements.txt     # Dependencias Python
│   ├── transcripciones/     # Carpeta de salida (se crea automáticamente)
│   └── templates/
│       └── index.html       # Interfaz web (frontend)
└── README.md
```

---

## Requisitos previos

### 1. Python
Versión 3.9 o superior. Verificar con:
```bash
python --version
```

### 2. ffmpeg
Whisper lo necesita para extraer el audio del video.

**Instalar con winget:**
```bash
winget install ffmpeg
```

> Si ya está instalado pero Python no lo encuentra, la ruta se configura directamente en `app.py` (ver sección de configuración).

### 3. Dependencias Python
Desde la carpeta `transcriber/`:
```bash
pip install -r requirements.txt
```

Esto instala:
| Paquete | Uso |
|---|---|
| `flask` | Servidor web |
| `openai-whisper` | Motor de transcripción |
| `ffmpeg-python` | Bindings de ffmpeg para Python |

---

## Configuración

### Ruta de ffmpeg (`app.py`, línea 10)
Si ffmpeg no está en el PATH del sistema, se configura manualmente:

```python
FFMPEG_BIN = r"C:\Users\<usuario>\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_...\bin"
```

Reemplaza `<usuario>` con tu nombre de usuario de Windows. Para encontrar la ruta exacta:
```powershell
Get-ChildItem -Path "$env:LOCALAPPDATA" -Recurse -Filter "ffmpeg.exe" -ErrorAction SilentlyContinue | Select-Object FullName
```

### Modelo de Whisper (`app.py`, línea 22)
```python
model = whisper.load_model("base")
```

Opciones disponibles, de menor a mayor precisión (y tiempo de procesamiento):

| Modelo | Velocidad | Precisión | VRAM requerida |
|---|---|---|---|
| `tiny` | Muy rápido | Básica | ~1 GB |
| `base` | Rápido | Buena ✅ (default) | ~1 GB |
| `small` | Moderado | Mejor | ~2 GB |
| `medium` | Lento | Alta | ~5 GB |
| `large` | Muy lento | Máxima | ~10 GB |

> En CPU (sin GPU), se usa FP32 automáticamente. El warning `FP16 is not supported on CPU` es normal y no afecta el resultado.

---

## Uso

### 1. Agregar videos
Coloca los archivos `.mp4` en la carpeta `Videos/`:
```
Transcriptions/
└── Videos/
    ├── reunion_enero.mp4
    └── presentacion.mp4
```

### 2. Iniciar el servidor
Desde la carpeta `transcriber/`:
```bash
python app.py
```

Salida esperada:
```
* Running on http://127.0.0.1:5000
```

### 3. Abrir la interfaz
Navega a [http://localhost:5000](http://localhost:5000) en el navegador.

### 4. Transcribir
1. Selecciona un video del dropdown (lista todos los `.mp4` de la carpeta `Videos/`)
2. Haz clic en **Transcribir**
3. Espera el procesamiento (puede tardar varios minutos según el largo del video)
4. La transcripción aparece en pantalla y se guarda automáticamente

---

## Salida

Cada transcripción se guarda automáticamente en:
```
transcriber/transcripciones/<nombre_del_video>.txt
```

Ejemplo: `Videos/reunion_enero.mp4` → `transcripciones/reunion_enero.txt`

Además, desde la UI puedes:
- **Copiar** el texto al portapapeles
- **Descargar** el `.txt` manualmente

---

## API endpoints

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/` | Sirve la interfaz web |
| `GET` | `/videos` | Lista los `.mp4` disponibles en `Videos/` |
| `POST` | `/transcribe` | Transcribe el video indicado |

### `POST /transcribe`

**Request body (JSON):**
```json
{
  "filename": "reunion_enero.mp4"
}
```

**Response exitosa:**
```json
{
  "transcript": "Texto completo de la transcripción...",
  "language": "es",
  "file_size_gb": 1.24
}
```

**Response de error:**
```json
{
  "error": "Descripción del error"
}
```

---

## Consideraciones de rendimiento

- El procesamiento ocurre **100% en local**, sin enviar datos a ningún servidor externo.
- En CPU, el tiempo de transcripción es aproximadamente **1x–4x la duración del video** dependiendo del modelo y el hardware.
- Para videos muy largos (varias horas), se recomienda dejar el proceso corriendo en segundo plano y no cerrar la terminal.
- Si tienes GPU NVIDIA con CUDA, Whisper la detecta automáticamente y el procesamiento es significativamente más rápido.

---

## Solución de problemas

| Error | Causa | Solución |
|---|---|---|
| `[WinError 2] El sistema no puede encontrar el archivo` | ffmpeg no está en el PATH | Configura `FFMPEG_BIN` en `app.py` con la ruta absoluta |
| `No hay videos en la carpeta Videos/` | La carpeta está vacía o en la ruta incorrecta | Verifica que los `.mp4` estén en `Transcriptions/Videos/` |
| `FP16 is not supported on CPU` | Sin GPU disponible | Es un warning, no un error. El proceso continúa normalmente en FP32 |
| Transcripción muy lenta | Modelo grande en CPU | Cambia a modelo `tiny` o `base` en `app.py` |
| Puerto 5000 ocupado | Otro proceso usa el puerto | Cambia el puerto: `app.run(port=5001)` |
