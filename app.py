from flask import Flask, request, send_file
from PyPDF2 import PdfWriter

app = Flask(__name__)

@app.route("/")
def home():
    with open("index.html", "r") as f:
        return f.read()

@app.route("/merge", methods=["POST"])
def merge_pdfs():
    merger = PdfWriter()
    pdfs = []

    uploaded = request.files.getlist("pdffiles")
    n = len(uploaded)

    for i in range(n):
        pdfs.append(uploaded[i])

    for pdf in pdfs:
        merger.append(pdf)

    output = "merged-pdf.pdf"
    merger.write(output)
    merger.close()

    return send_file(output, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

