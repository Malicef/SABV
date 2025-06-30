from flask import Flask, session, redirect, url_for

from conf import configure_all

app = Flask(__name__)
app.secret_key = "chave_secreta_simples"

configure_all(app)

@app.route("/")
def home():
    return redirect(url_for("admin.login_admin"))

if __name__ == "__main__":
    app.run(debug=True, port=5002)
