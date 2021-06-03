import qrcode
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect


def buildQR(text):
    # имя конечного файла
    filename = "templates/site.png"
    # генерируем qr-код
    if text != 'site.png':
        img = qrcode.make(text)
        # сохраняем img в файл
        img.save(filename)

    return


app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        QRtext = request.form["QR"]
        return redirect(url_for("QRtext", text=QRtext))
    else:
        return render_template("index.html")


@app.route("/<text>")
def QRtext(text):
    buildQR(text)
    # print(text)
    return render_template("out.html")


if __name__ == "__main__":
    app.run(debug=True)
