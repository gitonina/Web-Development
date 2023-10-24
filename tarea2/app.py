from flask import Flask, request, render_template, redirect, url_for, session,flash
from flask_paginate import Pagination
from utils.validations import validate_register_user, validate_files
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
import uuid
UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)


app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/") #ruta que redirige a la pagina principal, que en mi caso seria index.html
def index():
    return render_template("pagina/index.html")


@app.route("/agregarartesano",methods=["POST","GET"]) #ruta para agregarartesano
def agregarartesano():
    if request.method == "POST":
        
        name = request.form.get("username")
        email = request.form.get("email")
        phone=request.form.get("phone")
        description=request.form.get("descripción")
        comuna=request.form.get("comuna")
        artesanias=request.form.get("artesanias")
        img = request.files.get("files")
        
        
        if  validate_register_user(name,email,phone) and validate_files(img) :
            db.register_artesano(comuna,description,name,email,phone)
            db.register_artesano_tipo(name,artesanias)
            
            _filename = hashlib.sha256(
            secure_filename(img.filename) # nombre del archivo
            .encode("utf-8") # encodear a bytes
            ).hexdigest()
            _extension = filetype.guess(img).extension
            img_filename = f"{_filename}_{str(uuid.uuid4())}.{_extension}"

        # 2. save img as a file
            img.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))

        # 3. save confession in db
           
            db.register_foto("static/uploads",img_filename,name)

        return redirect(url_for("index"))
    
    elif request.method=="GET":
         return render_template("pagina/agregar-artesano.html")
    



@app.route("/agregarhincha") #ruta para agregar hincha
def agregarhincha():
    return render_template("pagina/agregar-hincha.html")


@app.route("/listadohinchas") #ruta para ver el lsitado de hinchas 
def listadohinchas():
    return render_template("pagina/ver-hinchas.html")


@app.route("/listadoartesanos") #ruta para ver el listado de artesanos
def listadoartesanos():
    count=db.get_total()[0]
    page_num = request.args.get('page', 1, type=int)
    per_page = 5
    start_index = (page_num - 1) * per_page + 1
    data=db.get_artesanos(per_page,start_index-1)
    datafoto=db.get_fotos(per_page,start_index-1)
    end_index = min(start_index + per_page, count)
    if end_index > count:
        end_index = count

    pagination = Pagination(page=page_num, total=count, per_page=per_page,
                            display_msg=f"Mostrando registros {start_index} - {end_index} de un total de <strong>({count})</strong>")    
    
    return render_template("pagina/ver-artesanos.html",artesanos=data,pagination=pagination,fotos=datafoto)
  

@app.route("/infoartesano/<int:artesano_id>")
def infoartesano(artesano_id):
    artesano_info = db.get_info_artesano(artesano_id)
    return render_template("pagina/informacion-artesano.html", artesano_info=artesano_info)

@app.route("/infohincha")
def infohincha():
    return render_template("pagina/informacion-hincha.html")



if __name__ == "__main__":
    app.run(debug=True)
