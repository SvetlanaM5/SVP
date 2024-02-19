import os
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ime = request.form.get("ime")
        adresa = request.form.get("adresa")
        vrsta = request.form.get("vrsta")
        velicina = request.form.get("velicina")
      #  dodaci = request.form.getlist("dodaci")
        dodaci = []
        if "kecap" in request.form:
            dodaci.append(request.form.get("kecap"))
        if "origano" in request.form:
            dodaci.append(request.form.get("origano"))
       
        conn = sqlite3.connect(os.path.join(app.root_path, 'baza.db'))
        cur = conn.cursor()
       # cur.execute("INSERT INTO porudzbine (ime, adresa, vrsta, velicina, dodaci)" +
        #    " VALUES (ime=ime, adresa=adresa, vrsta=vrsta, velicina=velicina, dodaci=dodaci)")
        #cur.execute("INSERT INTO porudzbine (ime, adresa, vrsta, velicina, dodaci) VALUES (?, ?, ?, ?, ?)",
         #           (ime, adresa, vrsta, velicina, ', '.join(dodaci)))

        cur.execute("INSERT INTO porudzbine (ime, adresa, vrsta, velicina, dodaci)" +
            " VALUES (:ime, :adresa, :vrsta, :velicina, :dodaci)",
            {"ime": ime, "adresa": adresa, "vrsta": vrsta, "velicina": velicina, "dodaci": ', '.join(dodaci)})

        conn.commit()  
        
        conn.close()
        
        return render_template("narudzbenica.html", ime=ime,
                               adresa=adresa, vrsta=vrsta,
                               velicina=velicina, dodaci=dodaci)   

    else:
        return render_template("formular.html")

   
