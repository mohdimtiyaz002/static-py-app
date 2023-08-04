from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/account", methods=["POST", "GET"])
def account():
    usr = "<User Not Defined>"
    if request.method == "POST":
        usr = request.form.get("name", "")
        if not usr:
            usr = "<User Not Defined>"
    return render_template("account.html", username=usr)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4949)
