import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import sounddevice as sd
import soundfile as sf
import numpy as np
import requests
import os
from datetime import datetime
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
CHANNELS = 1
WHISPER_MODEL = "small"
OLLAMA_MODEL = "llama3.1:8b"

recording = False
audio_chunks = []
recording_start_time = None
save_folder = os.getcwd()


def choose_folder():
    global save_folder

    folder = filedialog.askdirectory(title="Choisir le dossier de sauvegarde")

    if folder:
        save_folder = folder
        folder_label.config(text=f"Dossier : {save_folder}")


def update_datetime():
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    date_label.config(text=f"Date : {now}")
    app.after(1000, update_datetime)


def update_timer():
    if recording and recording_start_time:
        elapsed = datetime.now() - recording_start_time
        total_seconds = int(elapsed.total_seconds())

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        timer_label.config(
            text=f"Durée d'enregistrement : {hours:02d}:{minutes:02d}:{seconds:02d}"
        )

        app.after(1000, update_timer)


def start_recording():
    global recording, audio_chunks, recording_start_time

    recording = True
    audio_chunks = []
    recording_start_time = datetime.now()

    status_label.config(text="Enregistrement en cours...")
    timer_label.config(text="Durée d'enregistrement : 00:00:00")

    start_button.config(state="disabled")
    stop_button.config(state="normal")
    choose_button.config(state="disabled")

    update_timer()

    threading.Thread(target=record_audio, daemon=True).start()


def record_audio():
    def callback(indata, frames, time, status):
        if status:
            print(status)
        if recording:
            audio_chunks.append(indata.copy())

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        callback=callback
    ):
        while recording:
            sd.sleep(500)


def stop_recording():
    global recording
    recording = False

    status_label.config(text="Traitement IA en cours...")
    stop_button.config(state="disabled")

    threading.Thread(target=process_meeting, daemon=True).start()


def process_meeting():
    try:
        if not audio_chunks:
            messagebox.showwarning("Attention", "Aucun audio enregistré.")
            reset_buttons()
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        audio_file = os.path.join(save_folder, f"meeting_{timestamp}.wav")
        transcript_file = os.path.join(save_folder, f"transcript_{timestamp}.md")
        summary_file = os.path.join(save_folder, f"summary_{timestamp}.md")

        audio_data = np.concatenate(audio_chunks, axis=0)
        sf.write(audio_file, audio_data, SAMPLE_RATE)

        transcript = transcribe_audio(audio_file)

        with open(transcript_file, "w", encoding="utf-8") as f:
            f.write(transcript)

        summary = summarize_text(transcript)

        with open(summary_file, "w", encoding="utf-8") as f:
            f.write(summary)

        status_label.config(text="Résumé généré avec succès.")

        messagebox.showinfo(
            "Terminé",
            f"Fichiers générés :\n\n"
            f"Audio : {audio_file}\n\n"
            f"Transcription : {transcript_file}\n\n"
            f"Résumé : {summary_file}"
        )

    except Exception as e:
        messagebox.showerror("Erreur", str(e))
        status_label.config(text="Erreur pendant le traitement.")

    finally:
        reset_buttons()


def transcribe_audio(audio_file):
    model = WhisperModel(
        WHISPER_MODEL,
        device="cpu",
        compute_type="int8"
    )

    segments, info = model.transcribe(audio_file, beam_size=5)

    transcript = []
    for segment in segments:
        transcript.append(
            f"[{segment.start:.1f}s - {segment.end:.1f}s] {segment.text}"
        )

    return "\n".join(transcript)


def summarize_text(transcript):
    prompt = f"""
Tu es un assistant professionnel de réunion.

Génère un compte rendu clair, structuré et professionnel en français.

Structure obligatoire :

# Compte rendu de réunion

## Résumé exécutif

## Points clés discutés

## Décisions prises

## Actions à suivre

| Responsable | Action | Échéance | Priorité |
|---|---|---|---|

## Risques ou blocages

## Questions ouvertes

## Prochaines étapes

## Message court à partager avec l'équipe

Règles :
- Sois clair et synthétique.
- N'invente aucune information.
- Si une information manque, écris "Non spécifié".

Transcription :
{transcript}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=600
    )

    response.raise_for_status()
    return response.json()["response"]


def reset_buttons():
    start_button.config(state="normal")
    stop_button.config(state="disabled")
    choose_button.config(state="normal")


app = tk.Tk()
app.title("Meeting Assistant IA")
app.geometry("620x430")
app.resizable(False, False)

title_label = tk.Label(
    app,
    text="Meeting Assistant IA",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=15)

date_label = tk.Label(
    app,
    text="Date :",
    font=("Arial", 11)
)
date_label.pack(pady=5)

status_label = tk.Label(
    app,
    text="Prêt à enregistrer",
    font=("Arial", 12, "bold")
)
status_label.pack(pady=8)

timer_label = tk.Label(
    app,
    text="Durée d'enregistrement : 00:00:00",
    font=("Arial", 12)
)
timer_label.pack(pady=8)

choose_button = tk.Button(
    app,
    text="Choisir le dossier de sauvegarde",
    font=("Arial", 11),
    width=35,
    command=choose_folder
)
choose_button.pack(pady=8)

folder_label = tk.Label(
    app,
    text=f"Dossier : {save_folder}",
    font=("Arial", 9),
    wraplength=560,
    fg="gray"
)
folder_label.pack(pady=5)

start_button = tk.Button(
    app,
    text="Démarrer la réunion",
    font=("Arial", 12),
    width=32,
    height=2,
    command=start_recording
)
start_button.pack(pady=8)

stop_button = tk.Button(
    app,
    text="Arrêter et générer le résumé",
    font=("Arial", 12),
    width=32,
    height=2,
    state="disabled",
    command=stop_recording
)
stop_button.pack(pady=8)

warning_label = tk.Label(
    app,
    text="Assurez-vous d'avoir l'autorisation des participants avant l'enregistrement.",
    font=("Arial", 9),
    fg="red",
    wraplength=560
)
warning_label.pack(pady=10)

update_datetime()

app.mainloop()