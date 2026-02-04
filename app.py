from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secretkey"

USERNAME = "admin"
PASSWORD = "1234"


# ================= LOGIN =================
@app.route("/", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        if (
            request.form.get("username") == USERNAME and
            request.form.get("password") == PASSWORD
        ):
            session["user"] = USERNAME
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


# ================= DASHBOARD =================
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ================= INCIDENT REPORT =================
@app.route("/incident-report")
def incident_report():
    return render_template("incident_report.html")

@app.route("/investigation")
def investigation():
    return render_template("investigation.html")


# ================= FIRE PROTECTION MAIN =================
@app.route("/fire-protection")
def fire_exti():
    return render_template("fire_exti.html")


# ================= FIRE PROTECTION OVERVIEW PAGES =================
@app.route("/fire-extinguisher")
def fire_extinguisher():
    return render_template("fire_extinguisher.html")


@app.route("/emergency-light")
def emergency_light():
    return render_template("emergency_light.html")


@app.route("/emergency-exit")
def emergency_exit():
    return render_template("emergency_exit.html")


@app.route("/fire-cabinet")
def fire_cabinet():
    return render_template("fire_cabinet.html")


@app.route("/fdas")
def fdas():
    return render_template("fdas.html")


@app.route("/manual-bell")
def manual_bell():
    return render_template("manual_bell.html")


@app.route("/fire-suppression")
def fire_suppression():
    return render_template("fire_suppression.html")


# ================= OTHERS =================
@app.route("/concern")
def concern():
    return render_template("concern.html")


@app.route("/file")
def file_page():
    return render_template("file_page.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
