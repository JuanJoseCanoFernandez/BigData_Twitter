from flask_script import Manager
from aplicacion.app import app,db
from aplicacion.models import *
from getpass import getpass

manager = Manager(app)
app.config['DEBUG'] = True # Ensure debugger will load.

@manager.command
def create_tables():
    "Create relational database tables."
    db.create_all()
    categoria=Categorias(id=0,nombre="Todos")
    db.session.add(categoria)
    db.session.commit()

@manager.command
def drop_tables():
    "Drop all project relational database tables. THIS DELETES DATA."
    db.drop_all()

@manager.command
def add_data_tables():
    db.create_all()

    categorias = ("Graficas","Archivos")
    for cat in categorias:
        categoria=Categorias(nombre=cat)
        db.session.add(categoria)
        db.session.commit()

@manager.command
def create_admin():
    usuario={"username":input("Usuario:"),
            "password":getpass("Password:"),
            "nombre":input("Nombre completo:"),
            "email":input("Email:"),
            "admin": True}
    usu=Usuarios(**usuario)
    db.session.add(usu)
    db.session.commit()

if __name__ == '__main__':
    manager.run()