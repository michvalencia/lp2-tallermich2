import json
import os
from flask import current_app
from app.extensions import db
from app.models import Categoria, Producto

def registrar_comandos(app):
    
    @app.cli.command("init-db")
    def init_db():
        """Crea las tablas en la base de datos."""
        db.create_all()
        print("¡Base de datos inicializada con éxito!")

    @app.cli.command("reset-db")
    def reset_db():
        """Borra todas las tablas y las vuelve a crear."""
        respuesta = input("¿Estás segura de reiniciar la base de datos? Se perderán los datos (s/n): ")
        if respuesta.lower() == 's':
            db.drop_all()
            db.create_all()
            print("¡Base de datos reiniciada (reset) correctamente!")
        else:
            print("Operación cancelada.")

    @app.cli.command("seed-db")
    def seed_db():
        """Lee el archivo JSON y puebla la base de datos."""
        json_path = os.path.join(current_app.root_path, 'data', 'productos.json')
        
        if not os.path.exists(json_path):
            print(f"No se encontró el archivo de datos en: {json_path}")
            return

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        count_nuevos = 0
        for item in data:
            sku = item.get("sku")
            
            # Evitar duplicados por SKU
            producto_existente = Producto.query.filter_by(sku=sku).first()
            if producto_existente:
                print(f"-> Producto con SKU {sku} ya existe. Omitiendo...")
                continue

            nombre_cat = item.get("categoria")
            
            # Buscar categoría o crearla si no existe
            categoria = Categoria.query.filter_by(nombre=nombre_cat).first()
            if not categoria:
                categoria = Categoria(nombre=nombre_cat)
                db.session.add(categoria)
                db.session.flush() # Envía el insert temporal para obtener el id

            # Crear el objeto Producto
            nuevo_prod = Producto(
                sku=sku,
                marca=item.get("marca"),
                nombre=item.get("nombre"),
                precio=item.get("precio"),
                foto=item.get("foto"),
                stock=item.get("stock", 0),
                activo=item.get("activo", True),
                categoria_id=categoria.id
            )
            
            db.session.add(nuevo_prod)
            count_nuevos += 1

        db.session.commit()
        print(f"¡Se han importado {count_nuevos} productos nuevos con éxito!")
