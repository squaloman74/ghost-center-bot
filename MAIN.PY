import sys
import os

from engine_core import GhostEngine


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <percorso_file_audio>")
        sys.exit(1)

    audio_path = sys.argv[1]

    if not os.path.isfile(audio_path):
        print(f"Errore: file audio non trovato: {audio_path}")
        sys.exit(1)

    try:
        engine = GhostEngine(input_audio_path=audio_path)
        result = engine.run()

        print("\n✅ Analisi completata con successo.")
        print(f"Spettrogramma: {result['spectrogram']}")
        print(f"Video:        {result['video']}")
        print(f"PDF:          {result['pdf']}")
    except Exception as e:
        print(f"\n❌ Errore durante l'esecuzione della pipeline: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

