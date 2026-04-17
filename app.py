from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    value = int(data.get("value", 5))

    if value <= 3:
        message = "Take a breath. Try slowing things down."
    elif value <= 7:
        message = "Pause and reset. Maybe step away for a minute."
    else:
        message = "You're doing great. Keep it up."

    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True)