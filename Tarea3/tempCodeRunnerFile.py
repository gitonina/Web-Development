@app.route("/infoartesano/<int:artesano_id>")
def infoartesano(artesano_id):
    artesano_info = db.get_info_artesano(artesano_id)
    return render_template("pagina/informacion-artesano.html", artesano_info=artesano_info)