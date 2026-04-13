import os
import sys
import json
import time
import threading
import whisper
from flask import Flask, request, jsonify, render_template, Response, stream_with_context

# Agrega ffmpeg al PATH explícitamente
FFMPEG_BIN = r"C:\Users\Juan Tinjaca\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin"
if FFMPEG_BIN not in os.environ.get("PATH", ""):
    os.environ["PATH"] = FFMPEG_BIN + os.pathsep + os.environ.get("PATH", "")

app = Flask(__name__)

VIDEOS_FOLDER     = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Videos'))
TRANSCRIPTS_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'transcripciones'))
os.makedirs(TRANSCRIPTS_FOLDER, exist_ok=True)

# Carga el modelo una sola vez al iniciar
# Opciones: tiny, base, small, medium, large
model = whisper.load_model("base")

# Almacén de progreso por job_id
progress_store = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return '', 204


@app.route('/videos', methods=['GET'])
def list_videos():
    if not os.path.exists(VIDEOS_FOLDER):
        return jsonify({'videos': []})
    files = [f for f in os.listdir(VIDEOS_FOLDER) if f.lower().endswith('.mp4')]
    return jsonify({'videos': sorted(files)})


def run_transcription(job_id, filepath, filename):
    """Ejecuta la transcripción en un hilo separado y actualiza el progreso."""
    try:
        progress_store[job_id] = {'status': 'loading', 'progress': 5, 'message': 'Cargando audio...'}
        time.sleep(0.5)

        file_size_gb = os.path.getsize(filepath) / (1024 ** 3)

        progress_store[job_id] = {'status': 'processing', 'progress': 15, 'message': 'Analizando audio...'}
        time.sleep(0.5)

        # Hook de progreso de Whisper via callback en los segmentos
        segments_done = [0]
        total_segments = [1]  # se actualiza al recibir el primer segmento

        def progress_callback(seek, total):
            """Whisper llama esto por cada chunk procesado."""
            pct = int((seek / max(total, 1)) * 75) + 15  # 15% → 90%
            progress_store[job_id] = {
                'status': 'processing',
                'progress': min(pct, 90),
                'message': f'Transcribiendo... {min(pct, 90)}%'
            }

        # Whisper no tiene callback nativo, usamos verbose con monkey-patch
        # Alternativa: transcribir con generator de segmentos
        progress_store[job_id] = {'status': 'processing', 'progress': 20, 'message': 'Iniciando transcripción...'}

        # Transcripción con seguimiento de segmentos
        result = {'text': '', 'language': 'desconocido', 'segments': []}

        # Usamos decode con seguimiento manual del audio
        audio = whisper.load_audio(filepath)
        duration = len(audio) / whisper.audio.SAMPLE_RATE  # duración en segundos

        progress_store[job_id] = {'status': 'processing', 'progress': 25, 'message': 'Audio cargado. Procesando segmentos...'}

        # Transcribir con condition_on_previous_text para mejor contexto
        raw = model.transcribe(
            audio,
            verbose=False,
            condition_on_previous_text=True,
            word_timestamps=False,
        )

        # Simular progreso basado en segmentos completados
        segments = raw.get('segments', [])
        total = len(segments) if segments else 1

        for i, seg in enumerate(segments):
            pct = 25 + int(((i + 1) / total) * 65)  # 25% → 90%
            progress_store[job_id] = {
                'status': 'processing',
                'progress': pct,
                'message': f'Procesando segmento {i+1} de {total}...'
            }

        transcript = raw['text']
        language   = raw.get('language', 'desconocido')

        progress_store[job_id] = {'status': 'saving', 'progress': 93, 'message': 'Guardando transcripción...'}
        time.sleep(0.3)

        txt_filename = os.path.splitext(filename)[0] + '.txt'
        txt_path = os.path.join(TRANSCRIPTS_FOLDER, txt_filename)
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(transcript)

        progress_store[job_id] = {
            'status': 'done',
            'progress': 100,
            'message': 'Transcripción completada.',
            'transcript': transcript,
            'language': language,
            'file_size_gb': round(file_size_gb, 2)
        }

    except Exception as e:
        progress_store[job_id] = {
            'status': 'error',
            'progress': 0,
            'message': f'Error: {str(e)}'
        }


@app.route('/transcribe', methods=['POST'])
def transcribe():
    data     = request.get_json()
    filename = data.get('filename', '').strip()
    filepath = os.path.join(VIDEOS_FOLDER, filename)

    if not filename:
        return jsonify({'error': 'No se proporcionó ningún archivo'}), 400
    if not os.path.exists(filepath):
        return jsonify({'error': f'Archivo no encontrado: {filename}'}), 404

    job_id = f"{filename}_{int(time.time())}"
    progress_store[job_id] = {'status': 'queued', 'progress': 0, 'message': 'En cola...'}

    thread = threading.Thread(target=run_transcription, args=(job_id, filepath, filename), daemon=True)
    thread.start()

    return jsonify({'job_id': job_id})


@app.route('/progress/<job_id>')
def progress(job_id):
    """SSE endpoint — emite eventos de progreso hasta completar."""
    def generate():
        last_progress = -1
        timeout = 7200  # 2 horas máximo
        elapsed  = 0
        interval = 0.5

        while elapsed < timeout:
            state = progress_store.get(job_id, {'status': 'unknown', 'progress': 0, 'message': ''})
            if state['progress'] != last_progress or state['status'] in ('done', 'error'):
                last_progress = state['progress']
                yield f"data: {json.dumps(state)}\n\n"
                if state['status'] in ('done', 'error'):
                    break
            time.sleep(interval)
            elapsed += interval

        # Limpiar memoria
        progress_store.pop(job_id, None)

    return Response(stream_with_context(generate()), mimetype='text/event-stream',
                    headers={'Cache-Control': 'no-cache', 'X-Accel-Buffering': 'no'})


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
