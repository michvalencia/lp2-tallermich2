from flask import Blueprint, render_template, abort
from app.models import Producto, Categoria

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    productos = Producto.query.filter_by(activo=True).all()
    categorias = Categoria.query.all()
    return render_template('index.html', productos=productos, categorias=categorias)

@main_bp.route('/producto/<int:id>')
def detalle_producto(id):
    producto = Producto.query.get_or_404(id)
    return render_template('detalle.html', producto=producto)

@main_bp.route('/categoria/<int:id>')
def productos_por_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    categorias = Categoria.query.all()
    productos = [p for p in categoria.productos if p.activo]
    return render_template('categorias.html', categoria=categoria, productos=productos, categorias=categorias)
