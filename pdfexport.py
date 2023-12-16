from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def export_to_pdf(release_note, filename="release_note.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.drawString(100, height - 100, release_note.title)
    c.drawString(100, height - 120, f"Release Date: {release_note.release_date}")
    c.drawString(100, height - 140, f"Summary: {release_note.summary}")

    y_position = height - 160
    c.drawString(100, y_position, "Features:")
    for feature in release_note.features:
        y_position -= 20
        c.drawString(120, y_position, f"- {feature}")

    y_position -= 40
    c.drawString(100, y_position, "Bug Fixes:")
    for bug_fix in release_note.bug_fixes:
        y_position -= 20
        c.drawString(120, y_position, f"- {bug_fix}")

    c.save()

# Export the release note as PDF
export_to_pdf(release_note)
