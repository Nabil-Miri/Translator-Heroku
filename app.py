import logging
import os

from flask import Flask, render_template, request
from model import EnFrTranslator

app = Flask(__name__)
# define model path
model_path = 'model/2BiLSTM.h5'

# create instance
model = EnFrTranslator(model_path)
logging.basicConfig(level=logging.INFO)
@app.route("/hello")
def index():
    """Provide simple health check route."""
    return "Hello world!"
@app.route("/", methods=["GET", "POST"])
def translate():
    """Provide main prediction API route. Responds to both GET and POST requests."""
    logging.info("Predict request received!")

    if request.method == 'POST':
        sentence = request.form["text"]A
        prediction = model.translate(sentence)
        logging.info("prediction from model= {}".format(prediction))
        return render_template('HTML.html', prediction = prediction)
    else:
        return render_template('HTML.html', prediction = "")


def main():
    """Run the Flask app."""
    port = os.environ.get('PORT', 8000)
    app.run(port=port, debug=False, host="0.0.0.0")

if __name__ == "__main__":
    main()