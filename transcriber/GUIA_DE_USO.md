# 🎙️ Guía de Uso — Blend Transcriptor

## ¿Qué es esta herramienta?

Blend Transcriptor convierte el audio de tus **videos (.mp4)** y **audios (.mp3)** en texto escrito de forma automática. Todo funciona en tu computador, sin internet y sin límites.

**Ejemplo:** Tienes una grabación de una reunión de 45 minutos → la herramienta te entrega un documento de texto con todo lo que se dijo.

---

## 📋 Antes de empezar (solo la primera vez)

Estas cosas ya deben estar instaladas en tu equipo. Si no estás seguro, pídele ayuda al equipo técnico:

| Requisito | ¿Para qué sirve? |
|-----------|-------------------|
| Python | Es el motor que hace funcionar la herramienta |
| ffmpeg | Permite extraer el audio de los videos |
| Las dependencias del proyecto | Librerías adicionales que necesita la herramienta |

> 💡 **Si ya usaste la herramienta antes, no necesitas hacer nada de esto de nuevo.**

---

## 🚀 Paso a paso: Cómo transcribir un archivo

### Paso 1 — Coloca tu archivo en la carpeta correcta

Copia el archivo que quieres transcribir (`.mp4` o `.mp3`) dentro de esta carpeta:

```
📁 transcriber → 📁 Videos
```

La ruta completa en tu computador es:
```
C:\Users\Juan Tinjaca\Documents\Repos\bnd_transcriber\transcriber\Videos\
```

> 💡 **Tip:** Puedes arrastrar el archivo directamente a la carpeta desde el explorador de archivos.

---

### Paso 2 — Inicia la herramienta

1. Abre una **terminal** (busca "cmd" o "Símbolo del sistema" en el menú de inicio)
2. Escribe estos comandos uno por uno y presiona Enter después de cada uno:

```
cd C:\Users\Juan Tinjaca\Documents\Repos\bnd_transcriber\transcriber
python app.py
```

3. Espera hasta que veas un mensaje como este:

```
 * Running on http://127.0.0.1:5000
```

> ⚠️ **No cierres esta ventana negra mientras estés usando la herramienta.** Si la cierras, la herramienta se apaga.

---

### Paso 3 — Abre la interfaz en tu navegador

Abre tu navegador (Chrome, Edge, Firefox) y escribe en la barra de direcciones:

```
http://localhost:5000
```

Verás una pantalla oscura con el título **"Blend — Transcriptor de Audio & Video"**.

---

### Paso 4 — Selecciona tu archivo

1. Haz clic en el menú desplegable que dice **"-- Selecciona un archivo --"**
2. Elige el archivo que colocaste en la carpeta Videos
3. Haz clic en el botón azul **"Transcribir"**

---

### Paso 5 — Espera la transcripción

Verás una barra de progreso que te muestra en qué etapa va:

| Etapa | Qué está pasando |
|-------|------------------|
| 🔵 **Carga** | Leyendo el archivo |
| 🔵 **Análisis** | Preparando el audio |
| 🔵 **Transcripción** | Convirtiendo audio a texto (la más larga) |
| 🔵 **Guardado** | Guardando el resultado |

> ⏱️ **¿Cuánto tarda?** Depende de la duración del archivo. Un video de 1 hora puede tardar entre 1 y 4 horas si no tienes GPU. Archivos cortos (5-10 min) tardan unos minutos.

---

### Paso 6 — Obtén tu transcripción

Cuando termine, verás el texto completo en pantalla. Tienes dos opciones:

| Botón | Qué hace |
|-------|----------|
| 📋 **Copiar texto** | Copia todo el texto al portapapeles para pegarlo donde quieras |
| ⬇️ **Descargar .txt** | Descarga un archivo de texto con la transcripción |

Además, la transcripción se guarda automáticamente en:
```
📁 transcriber → 📁 transcripciones → tu_archivo.txt
```

---

## 🔄 Para transcribir otro archivo

Simplemente selecciona otro archivo del menú desplegable y haz clic en "Transcribir" de nuevo. No necesitas reiniciar nada.

---

## 🛑 Para apagar la herramienta

Ve a la ventana negra (terminal) donde iniciaste la herramienta y presiona:

```
Ctrl + C
```

---

## ❓ Preguntas frecuentes

### "No veo mi archivo en la lista"
→ Asegúrate de que el archivo esté en la carpeta `Videos` y que sea `.mp4` o `.mp3`. Si lo acabas de copiar, recarga la página del navegador (F5).

### "La página no carga"
→ Verifica que la ventana negra (terminal) siga abierta y muestre el mensaje "Running on...". Si se cerró, repite el Paso 2.

### "Dice 'Error de conexión con el servidor'"
→ La herramienta se apagó. Cierra la terminal, ábrela de nuevo y repite desde el Paso 2.

### "La transcripción está tardando mucho"
→ Es normal para archivos largos. No cierres la ventana ni el navegador. Puedes seguir trabajando en otras cosas mientras tanto.

### "El texto tiene errores"
→ La herramienta hace su mejor esfuerzo pero no es perfecta. Puede confundir palabras similares, especialmente con ruido de fondo o varios hablantes. Revisa y corrige lo que sea necesario.

### "Aparece un mensaje rojo de error"
→ Toma una captura de pantalla del error y envíala al equipo técnico.

---

## 📁 Resumen de carpetas importantes

```
📁 transcriber/
├── 📁 Videos/            ← PON TUS ARCHIVOS AQUÍ
├── 📁 transcripciones/   ← AQUÍ SE GUARDAN LOS RESULTADOS
└── 🐍 app.py            ← La herramienta (no tocar)
```

---

## 🎯 Tips para mejores resultados

- **Audio claro** = mejor transcripción. Evita grabaciones con mucho ruido de fondo.
- **Un solo hablante** funciona mejor que varios hablando al tiempo.
- **Archivos más cortos** se procesan más rápido. Si tienes un video de 3 horas, considera cortarlo.
- La herramienta detecta el idioma automáticamente (español, inglés, etc.).

---

> 📞 **¿Necesitas ayuda?** Contacta al equipo técnico si algo no funciona como se describe aquí.
