import os
import subprocess


def generate_video(spectrogram_path, output_dir, timestamp):
    """
    Generate a simple video from the spectrogram image using FFmpeg.
    """

    video_path = os.path.join(output_dir, f"evp_video_{timestamp}.mp4")

    # FFmpeg command
    cmd = [
        "ffmpeg",
        "-y",
        "-loop", "1",
        "-i", spectrogram_path,
        "-c:v", "libx264",
        "-t", "10",
        "-pix_fmt", "yuv420p",
        video_path
    ]

    try:
        subprocess.run(cmd, check=True)
    except Exception as e:
        raise RuntimeError(f"FFmpeg video generation failed: {str(e)}")

    return video_path

