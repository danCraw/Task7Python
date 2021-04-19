import qrcode
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect


def buildQR(text):
    # пример данных
    data = text
    # имя конечного файла
    filename = "templates/site.png"
    # генерируем qr-код
    img = qrcode.make(data)
    # сохраняем img в файл
    img.save(filename)


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
    return render_template("out.html")


if __name__ == "__main__":
    app.run(debug=True)
