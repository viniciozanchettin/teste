from flask import Flask, render_template, request, redirect, url_for, flash

def create_app():
    app = Flask(__name__)
    app.config.update(SECRET_KEY="change-me")

    @app.get("/")
    def index():
        return render_template("index.html", title="Home")

    @app.get("/about")
    def about():
        return render_template("about.html", title="Sobre")

    @app.post("/echo")
    def echo():
        name = request.form.get("name", "").strip() or "Mundo"
        flash(f"Olá, {name}! 👋")
        return redirect(url_for("index"))

    return app

# Para `flask --app app.app run`
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)