import pymysql
import json

DB_NAME = "tarea2"
DB_USERNAME = "root"
DB_PASSWORD = "programacionweb_dcc"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

with open('database/querys.json', 'r') as querys:
	QUERY_DICT = json.load(querys)

# -- conn ---

def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn

# -- querys --

def get_artesano_by_id(name):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_user_by_id"], (name,))
	user = cursor.fetchone()
	return user

def get_hincha_by_id(name):
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["get_hincha_by_id"],(name,))
	user=cursor.fetchone()
	return user

def get_artesano_by_email(email):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_artesano_by_email"], (email,))
	user = cursor.fetchone()
	return user

def get_artesano_by_username(username):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_artesano_by_username"], (username,))
	user = cursor.fetchone()
	return user

def get_artesano_by_comuna(comuna):
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["get_artesano_by_comuna"],(comuna,))
	user=cursor.fetchone()
	return user


def get_hincha_by_comuna(comuna):
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["get_hincha_by_comuna"],(comuna,))
	user=cursor.fetchone()
	return user

def get_total():
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["get_total"],())
	count=cursor.fetchone()
	return count 

def get_total_hincha():
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["get_total_hincha"],())
	count=cursor.fetchone()
	return count 


def get_artesanos(a,b):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_artesanos"], (a,b))
	confessions = cursor.fetchall()
	return confessions

def get_hinchas(a,b):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_hinchas"], (a,b))
	confessions = cursor.fetchall()
	return confessions


def get_fotos(a,b):
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["get_fotos"], (a,b))
	confessions=cursor.fetchall()
	return confessions


def get_info_hinchas(a,b):
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["get_info_hinchas"], (a,b))
	confessions=cursor.fetchall()
	return confessions



def get_artesania_id(name):
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["get_artesania_id"],(name,))
	user=cursor.fetchone()
	return user

def get_deporte_id(name):
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["get_deporte_id"],(name,))
	user=cursor.fetchone()
	return user

def get_info_artesano(artesano_id):
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["get_info_artesano"],(artesano_id))
	user=cursor.fetchone()
	return user
	

def get_hincha_info(hincha_id):
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["get_hincha_info"],(hincha_id))
	user=cursor.fetchone()
	return user



def get_stats_data_from_db():
    conn = get_conn()
    cursor = conn.cursor()
    

    cursor.execute("""
        SELECT tipo_artesania.nombre AS tipo, COUNT(*) AS artesanos
        FROM tipo_artesania
        JOIN artesano_tipo ON tipo_artesania.id = artesano_tipo.tipo_artesania_id
        GROUP BY tipo_artesania.nombre
    """)

  
    data = []
    for row in cursor.fetchall():
        tipo, artesanos = row
        data.append({"tipo": tipo, "artesanos": artesanos})

   
    cursor.close()
    conn.close()

    return data


def get_hincha_stats_data_from_db():
    conn = get_conn()
    cursor = conn.cursor()
    
    cursor.execute("""
       SELECT deporte.nombre AS tipo, COUNT(*) AS hinchas
       FROM deporte
       JOIN hincha_deporte ON deporte.id = hincha_deporte.deporte_id
	   GROUP BY deporte.nombre
    """)


    data = []
    for row in cursor.fetchall():
        tipo, hinchas = row
        data.append({"tipo": tipo, "hinchas": hinchas})

    cursor.close()
    conn.close()

    return data


def create_artesano(comuna_id,descripcion_artesania, nombre, email, celular):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["create_artesano"], (comuna_id,descripcion_artesania,nombre,email,celular))
	conn.commit()



def create_hincha(comuna_id,transporte,nombre,email,celular,comentarios):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["create_hincha"], (comuna_id,transporte,nombre,email,celular,comentarios))
	conn.commit()

def create_region(nombre):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["create_region"], (nombre,))
	conn.commit()


def create_comuna(region_id, id, nombre):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["create_comuna"], (region_id,id,nombre))
	conn.commit()



def create_foto(ruta_archivo, nombre_archivo, artesano_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["create_foto"], (ruta_archivo, nombre_archivo, artesano_id))
	conn.commit()

def create_artesano_tipo(artesano_id,tipo_artesania_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["create_artesano_tipo"], (artesano_id,tipo_artesania_id))
	conn.commit()

def create_hincha_deporte(hincha_id,deporte_id):
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["create_hincha_deporte"],(hincha_id,deporte_id))
	conn.commit()
# -- db-related functions --






#funcion para registrar un artesano
def register_artesano(comuna,descripcion_artesania, nombre, email, celular):
	# 1. check the email is not in use
	_email_user = get_artesano_by_email(email)
	comuna_id=get_artesano_by_comuna(comuna)
	if _email_user is not None:
		return False, "El correo ya esta en uso."
	# 2. check the username is not in use
	_username_user = get_artesano_by_username(nombre)
	if _username_user is not None:
		return False, "El nombre de usuario esta en uso."
	# 3. create user
	create_artesano(comuna_id,descripcion_artesania,nombre,email,celular)
	return True, None



def register_hincha(comuna, transporte, nombre, email, celular, comentarios):
    comuna_id = get_hincha_by_comuna(comuna)
    create_hincha(comuna_id, transporte, nombre, email, celular, comentarios)
    return True, None



def register_artesano_tipo(artesano_id, tipo_artesania_id):
    artesano = get_artesano_by_id(artesano_id)
    artesania = get_artesania_id(tipo_artesania_id)
    create_artesano_tipo(artesano, artesania)
    return True, None


def register_foto(ruta,nombre,artesano_id):
	artesano=get_artesano_by_id(artesano_id)
	create_foto(ruta,nombre,artesano)
	return True,None

def register_hincha_deporte(name, deporte):
    hincha_id = get_hincha_by_id(name)
    deporte_id = get_deporte_id(deporte)
    create_hincha_deporte(hincha_id,deporte_id)
    return True, None

