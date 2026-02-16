import os
import logging
from datetime import datetime

from spectrogram import generate_spectrogram
from video_generator import generate_video
from pdf_report import generate_pdf_report
from telegram_sender import send_telegram_message
from database import save_analysis_record
from utils import ensure_output_dir, load_audio_file


class GhostEngine:
    def __init__(self, input_audio_path, output_dir="evp_analysis_output"):
        self.input_audio_path = input_audio_path
        self.output_dir = ensure_output_dir(output_dir)
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Logging setup
        log_path = os.path.join(self.output_dir, f"engine_log_{self.timestamp}.txt")
        logging.basicConfig(
            filename=log_path,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        logging.info("GhostEngine initialized")

    def run(self):
        try:
            logging.info("Starting analysis pipeline")

            # Load audio
            audio_data, sr = load_audio_file(self.input_audio_path)
            logging.info("Audio loaded successfully")

            # Generate spectrogram
            spectrogram_path = generate_spectrogram(
                audio_data, sr, self.output_dir, self.timestamp
            )
            logging.info(f"Spectrogram saved: {spectrogram_path}")

            # Generate video
            video_path = generate_video(
                spectrogram_path, self.output_dir, self.timestamp
            )
            logging.info(f"Video saved: {video_path}")

            # Generate PDF report
            pdf_path = generate_pdf_report(
                spectrogram_path, video_path, self.output_dir, self.timestamp
            )
            logging.info(f"PDF report saved: {pdf_path}")

            # Save to database
            save_analysis_record(
                audio_path=self.input_audio_path,
                spectrogram_path=spectrogram_path,
                video_path=video_path,
                pdf_path=pdf_path,
                timestamp=self.timestamp
            )
            logging.info("Database record saved")

            # Send Telegram notification
            send_telegram_message(
                f"Analisi completata!\nSpettrogramma: {spectrogram_path}\nVideo: {video_path}\nPDF: {pdf_path}"
            )
            logging.info("Telegram notification sent")

            return {
                "spectrogram": spectrogram_path,
                "video": video_path,
                "pdf": pdf_path
            }

        except Exception as e:
            logging.error(f"Pipeline error: {str(e)}")
            raise RuntimeError(f"GhostEngine failed: {str(e)}")

