
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "virtual_machine_project"

# Project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "database.db")


# Database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Initialize database
def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS virtual_machines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            os TEXT NOT NULL,
            cpu INTEGER NOT NULL,
            ram INTEGER NOT NULL,
            status TEXT DEFAULT 'Stopped'
        )
    """)

    conn.commit()
    conn.close()


# Dashboard
@app.route("/")
def index():
    conn = get_db_connection()

    vms = conn.execute(
        "SELECT * FROM virtual_machines ORDER BY id DESC"
    ).fetchall()

    total_vms = len(vms)

    running_vms = sum(
        1 for vm in vms if vm["status"] == "Running"
    )

    stopped_vms = total_vms - running_vms

    total_cpu = sum(vm["cpu"] for vm in vms)
    total_ram = sum(vm["ram"] for vm in vms)

    conn.close()

    return render_template(
        "index.html",
        vms=vms,
        total_vms=total_vms,
        running_vms=running_vms,
        stopped_vms=stopped_vms,
        total_cpu=total_cpu,
        total_ram=total_ram
    )


# Create virtual machine
@app.route("/create", methods=["GET", "POST"])
def create_vm():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        os_name = request.form.get("os", "")

        try:
            cpu = int(request.form.get("cpu", 0))
            ram = int(request.form.get("ram", 0))
        except ValueError:
            flash("Invalid CPU or RAM value.", "error")
            return redirect(url_for("create_vm"))

        if not name or not os_name or cpu < 1 or ram < 1:
            flash("Please enter valid VM details.", "error")
            return redirect(url_for("create_vm"))

        conn = get_db_connection()

        conn.execute("""
            INSERT INTO virtual_machines
            (name, os, cpu, ram, status)
            VALUES (?, ?, ?, ?, 'Stopped')
        """, (name, os_name, cpu, ram))

        conn.commit()
        conn.close()

        flash("Virtual machine created successfully!", "success")

        return redirect(url_for("index"))

    return render_template("create_vm.html")


# Start virtual machine
@app.route("/start/<int:vm_id>")
def start_vm(vm_id):

    conn = get_db_connection()

    conn.execute(
        "UPDATE virtual_machines SET status = 'Running' WHERE id = ?",
        (vm_id,)
    )

    conn.commit()
    conn.close()

    flash("Virtual machine started successfully!", "success")

    return redirect(url_for("index"))


# Stop virtual machine
@app.route("/stop/<int:vm_id>")
def stop_vm(vm_id):

    conn = get_db_connection()

    conn.execute(
        "UPDATE virtual_machines SET status = 'Stopped' WHERE id = ?",
        (vm_id,)
    )

    conn.commit()
    conn.close()

    flash("Virtual machine stopped successfully!", "success")

    return redirect(url_for("index"))


# Delete virtual machine
@app.route("/delete/<int:vm_id>")
def delete_vm(vm_id):

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM virtual_machines WHERE id = ?",
        (vm_id,)
    )

    conn.commit()
    conn.close()

    flash("Virtual machine deleted successfully!", "success")

    return redirect(url_for("manage_vm"))


# Manage virtual machines
@app.route("/manage")
def manage_vm():

    conn = get_db_connection()

    vms = conn.execute(
        "SELECT * FROM virtual_machines ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template(
        "manage_vm.html",
        vms=vms
    )


# Hypervisor information
@app.route("/hypervisor")
def hypervisor():

    return render_template("hypervisor.html")


# Run application
if __name__ == "__main__":

    init_db()

    app.run(debug=True)