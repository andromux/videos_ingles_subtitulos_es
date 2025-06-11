import os
import srt
import ffmpeg
from datetime import timedelta
from faster_whisper import WhisperModel
from deep_translator import GoogleTranslator

# === CONFIGURACIÓN ===
VIDEO_INPUT = "traduciendo.mp4"
VIDEO_OUTPUT = "traduciendo_subtitulada.mp4"
SRT_FILE = "subtitulos.srt"
LANG_ORIG = "en"
LANG_TARGET = "es"
MODEL_SIZE = "base"  # Puedes usar "small" o "medium" si quieres mejor precisión

# === TRANSCRIPCIÓN ===
def transcribe_video(video_path):
    print("⏳ Transcribiendo video (sin censura)...")
    model = WhisperModel(MODEL_SIZE, compute_type="int8")
    segments, _ = model.transcribe(video_path, beam_size=5)
    return list(segments)

# === TRADUCCIÓN CON GOOGLE (local, sin censura explícita) ===
def translate_text(text):
    try:
        return GoogleTranslator(source=LANG_ORIG, target=LANG_TARGET).translate(text)
    except Exception as e:
        print("❌ Error en traducción:", e)
        return "[Error en traducción]"

# === GENERAR SUBTÍTULOS ===
def generate_translated_srt(segments, srt_path):
    print("🌍 Traduciendo y generando subtítulos...")
    subs = []
    for i, seg in enumerate(segments):
        start = timedelta(seconds=seg.start)
        end = timedelta(seconds=seg.end)

        original_text = seg.text.strip()
        translated_text = translate_text(original_text)

        content = translated_text

        subs.append(srt.Subtitle(index=i + 1, start=start, end=end, content=content))

    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(srt.compose(subs))

# === AÑADIR SUBTÍTULOS CON ESTILO (re-codificando video) ===
def add_subtitles_to_video(input_video, srt_file, output_video):
    print("🎬 Incrustando subtítulos en el video final...")
    ffmpeg.input(input_video).output(
        output_video,
        vf=(
            f"subtitles={srt_file}:force_style="
            "'FontName=Arial,FontSize=20,PrimaryColour=&H00FFFFFF,"
            "OutlineColour=&H00000000,BorderStyle=1,Outline=2,Shadow=1,Alignment=2'"
        ),
        vcodec="libx264",  # 🔧 necesario para aplicar filtros
        acodec="aac",      # 🔧 audio codificado común
        strict="-2"
    ).run(overwrite_output=True)

# === FLUJO PRINCIPAL ===
def main():
    segments = transcribe_video(VIDEO_INPUT)
    generate_translated_srt(segments, SRT_FILE)
    add_subtitles_to_video(VIDEO_INPUT, SRT_FILE, VIDEO_OUTPUT)
    print("✅ Proceso completo. Archivo generado:", VIDEO_OUTPUT)

if __name__ == "__main__":
    main()
