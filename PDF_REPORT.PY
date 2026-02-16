import os
from fpdf import FPDF


def generate_pdf_report(spectrogram_path, video_path, output_dir, timestamp):
    """
    Generate a clean PDF report containing the spectrogram and metadata.
    """

    pdf_path = os.path.join(output_dir, f"evp_report_{timestamp}.pdf")

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, "EVP Analysis Report", ln=True, align="C")

    pdf.ln(10)

    # Timestamp
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Timestamp: {timestamp}", ln=True)

    pdf.ln(5)

    # Spectrogram image
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Spectrogram:", ln=True)

    pdf.image(spectrogram_path, w=180)

    pdf.ln(10)

    # Video reference
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Generated Video:", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, f"Video file saved at:\n{video_path}")

    # Save PDF
    pdf.output(pdf_path)

    return pdf_path

