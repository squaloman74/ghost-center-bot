import os
import sqlite3


DB_PATH = "evp_analysis.db"


def _ensure_database():
    """Create database and table if not exists."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            audio_path TEXT,
            spectrogram_path TEXT,
            video_path TEXT,
            pdf_path TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_analysis_record(audio_path, spectrogram_path, video_path, pdf_path, timestamp):
    """Save a new analysis entry into the database."""
    _ensure_database()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO analysis (timestamp, audio_path, spectrogram_path, video_path, pdf_path)
        VALUES (?, ?, ?, ?, ?)
    """, (timestamp, audio_path, spectrogram_path, video_path, pdf_path))

    conn.commit()
    conn.close()

    return True

