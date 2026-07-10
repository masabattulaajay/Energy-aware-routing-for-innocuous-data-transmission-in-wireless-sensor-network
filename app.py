from flask import Flask, render_template, request, redirect, url_for, session

from algorithms.routing import Routing
from algorithms.vawgan import VAWGAN
from algorithms.npoa import NPOA
from algorithms.security import Security

from database.db import *

app = Flask(__name__)
app.secret_key = "WSN2026"

# ------------------------------------
# Initialize Database
# ------------------------------------
create_tables()
insert_default_user()

# ------------------------------------
# Create Objects
# ------------------------------------
routing = Routing()
vawgan = VAWGAN()
npoa = NPOA()
security = Security()


# ====================================
# HOME
# ====================================
@app.route("/")
def home():
    return render_template("index.html")


# ====================================
# LOGIN
# ====================================
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = validate_login(username, password)

        if user:

            session["user"] = username

            return redirect(url_for("dashboard"))

        else:

            return render_template(
                "login.html",
                msg="Invalid Username or Password"
            )

    return render_template("login.html")


# ====================================
# DASHBOARD
# ====================================
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")


# ====================================
# NETWORK
# ====================================
@app.route("/network", methods=["GET", "POST"])
def network():

    if "user" not in session:
        return redirect(url_for("login"))

    nodes = None

    if request.method == "POST":

        total = int(request.form["nodes"])

        nodes = routing.create_network(total)

        save_nodes(nodes)

    return render_template(
        "network.html",
        nodes=nodes
    )


# ====================================
# VAWGAN DETECTION
# ====================================
@app.route("/detection")
def detection():

    if "user" not in session:
        return redirect(url_for("login"))

    nodes = get_nodes()

    malicious_nodes = vawgan.detect_malicious_nodes(nodes)

    accuracy = vawgan.detection_accuracy()

    fpr = vawgan.false_positive_rate()

    detection_time = vawgan.detection_time()

    return render_template(
        "detection.html",
        malicious=len(malicious_nodes),
        accuracy=accuracy,
        fpr=fpr,
        detection_time=detection_time
    )


# ====================================
# NPOA ROUTING
# ====================================
@app.route("/routing")
def routing_page():

    if "user" not in session:
        return redirect(url_for("login"))

    nodes = get_nodes()

    route = npoa.select_route(nodes)

    energy = npoa.route_energy()

    delay = npoa.transmission_delay()

    throughput = npoa.throughput()

    pdr = npoa.packet_delivery_ratio()

    route_text = " → ".join(
        [f"Node {x}" for x in route]
    )

    return render_template(
        "routing.html",
        route=route_text,
        energy=energy,
        delay=delay,
        throughput=throughput,
        pdr=pdr
    )


# ====================================
# TRANSMISSION
# ====================================
@app.route("/transmission", methods=["GET", "POST"])
def transmission():

    if "user" not in session:
        return redirect(url_for("login"))

    encrypted = ""
    decrypted = ""
    hash_value = ""
    status = ""

    if request.method == "POST":

        message = request.form["message"]

        encrypted = security.encrypt(message)

        decrypted = security.decrypt(encrypted)

        hash_value = security.generate_hash(message)

        status = security.transmission_status()

        save_transmission(
            "Node 1",
            "Node 10",
            message,
            encrypted,
            "Optimal Route",
            status
        )

    return render_template(
        "transmission.html",
        encrypted=encrypted,
        decrypted=decrypted,
        hash_value=hash_value,
        status=status
    )


# ====================================
# RESULT
# ====================================
@app.route("/result")
def result():

    if "user" not in session:
        return redirect(url_for("login"))

    nodes = get_nodes()

    energy = routing.average_energy()

    delay = npoa.transmission_delay()

    throughput = npoa.throughput()

    pdr = npoa.packet_delivery_ratio()

    return render_template(
        "result.html",
        energy=energy,
        delay=delay,
        throughput=throughput,
        pdr=pdr
    )


# ====================================
# ABOUT
# ====================================
@app.route("/about")
def about():
    return render_template("about.html")


# ====================================
# LOGOUT
# ====================================
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# ====================================
# RUN
# ====================================
if __name__ == "__main__":
    app.run(debug=True)