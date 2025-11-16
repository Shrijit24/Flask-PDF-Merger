from flask import Flask, request, send_file
from PyPDF2 import PdfWriter

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="POST":
        num = request.form.get("num_files")
        if num and num.isdigit() and int(num) > 0:
            num = int(num)
            with open("upload.html","r") as f:
                html = f.read()
            inputs_html = ""
            for i in range(1,num+1):
                inputs_html += (f"File {i} : <input type='file' name='pdf{i}'><br><br>\n")
            html = html.replace("{{inputs}}",inputs_html)
            return html
        else:
            return ("Enter a valid number of files.")
    with open("index.html","r") as f:
        return f.read()

@app.route("/merge", methods=["POST"])
def merge():
    num = int(request.form.get("num_files"))
    merger = PdfWriter()
    for i in range(1,num+1):
        f = request.files.get(f"pdf{i}")
        if f:
            merger.append(f)
    output = ("merged.pdf")
    merger.write(output)
    merger.close()
    return send_file(output, as_attachment=True)

if __name__=="__main__":
    app.run(debug=True)



