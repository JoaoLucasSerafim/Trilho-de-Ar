
from flask import Flask, render_template, request
 
app = Flask(__name__)
 
def velocidade(ds, dt):
    return ds / dt
 
@app.route("/", methods=["GET", "POST"])
def home():
    resultados = None
 
    if request.method == "POST":
        try:
            t1 = float(request.form["P1"])
            t2 = float(request.form["P2"])
            t3 = float(request.form["P3"])
            t4 = float(request.form["P4"])
 
            # Velocidade entre cada sensor (ΔS = 10cm fixo)
            v1 = velocidade(10, t1 - 0)
            v2 = velocidade(10, t2 - t1)
            v3 = velocidade(10, t3 - t2)
            v4 = velocidade(10, t4 - t3)
 
            # Velocidade média total
            v_media = velocidade(40, t4 - 0)
 
            resultados = {
                "v1": round(v1, 2),
                "v2": round(v2, 2),
                "v3": round(v3, 2),
                "v4": round(v4, 2),
                "v_media": round(v_media, 2),
            }
        except ValueError:
            resultados = {"erro": "Insira apenas números válidos."}
 
    return render_template("index.html", resultados=resultados)
 
if __name__ == "__main__":
    app.run(debug=True)
