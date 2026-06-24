from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
import os
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    translated = ""

    if request.method == "POST":

        text = request.form["text"]

        source = request.form["source"]

        target = request.form["target"]

        try:

            translated = GoogleTranslator(
                source=source,
                target=target
            ).translate(text)

        except:

            translated = "Translation Failed"

    return render_template(
        "index.html",
        translated=translated
    )




if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )