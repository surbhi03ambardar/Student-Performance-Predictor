from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    study_hours = float(request.form["study_hours"])
    attendance = float(request.form["attendance"])

    score = (study_hours * 10) + (attendance * 0.4)

    if score > 100:
        score = 100

    return render_template(
        "index.html",
        prediction=round(score, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)