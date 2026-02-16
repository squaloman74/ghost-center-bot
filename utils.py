import os
import librosa
import soundfile as sf


def ensure_output_dir(path):
    """Ensure output directory exists."""
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def load_audio_file(audio_path):
    """Load audio file safely with fallback."""
    if not os.path.isfile(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    try:
        audio_data, sr = librosa.load(audio_path, sr=None, mono=True)
        return audio_data, sr
    except Exception:
        # Fallback using soundfile
        audio_data, sr = sf.read(audio_path)
        if len(audio_data.shape) > 1:
            audio_data = audio_data[:, 0]  # take first channel
        return audio_data, sr

