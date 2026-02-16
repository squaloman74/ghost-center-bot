import os
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display


def generate_spectrogram(audio_data, sr, output_dir, timestamp):
    """
    Generate a high‑quality spectrogram image.
    """

    # Output path
    spectrogram_path = os.path.join(output_dir, f"spectrogram_{timestamp}.png")

    # Create figure
    plt.figure(figsize=(14, 6))

    # Compute STFT
    stft = librosa.stft(audio_data, n_fft=2048, hop_length=512)
    stft_db = librosa.amplitude_to_db(np.abs(stft), ref=np.max)

    # Display spectrogram
    librosa.display.specshow(
        stft_db,
        sr=sr,
        hop_length=512,
        x_axis="time",
        y_axis="hz",
        cmap="magma"
    )

    plt.colorbar(format="%+2.0f dB")
    plt.title("EVP Spectrogram Analysis")
    plt.tight_layout()

    # Save image
    plt.savefig(spectrogram_path, dpi=300)
    plt.close()

    return spectrogram_path

