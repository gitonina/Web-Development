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


def get_total():
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["get_total"],())
	count=cursor.fetchone()
	return count 


def get_artesanos(a,b):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_artesanos"], (a,b))
	confessions = cursor.fetchall()
	return confessions


def get_fotos(a,b):
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["get_fotos"], (a,b))
	confessions=cursor.fetchall()
	return confessions


def get_artesania_id(name):
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["get_artesania_id"],(name,))
	user=cursor.fetchone()
	return user


def get_info_artesano(artesano_id):
	conn=get_conn()
	cursor=conn.cursor()
	cursor.execute(QUERY_DICT["get_info_artesano"],(artesano_id))
	user=cursor.fetchone()
	return user
	


def create_artesano(comuna_id,descripcion_artesania, nombre, email, celular):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["create_artesano"], (comuna_id,descripcion_artesania,nombre,email,celular))
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



def register_artesano_tipo(artesano_id, tipo_artesania_id):
    artesano = get_artesano_by_id(artesano_id)
    artesania = get_artesania_id(tipo_artesania_id)
    create_artesano_tipo(artesano, artesania)
    return True, None


def register_foto(ruta,nombre,artesano_id):
	artesano=get_artesano_by_id(artesano_id)
	create_foto(ruta,nombre,artesano)
	return True,None
