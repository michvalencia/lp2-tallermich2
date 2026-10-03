from flask import Blueprint, render_template, request, abort

from app.models import Producto, Categoria

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    categoria_id = request.args.get('categoria', type=int)

    if categoria_id:
        productos = Producto.query.filter_by(categoria_id=categoria_id, activo=True).all()
    else:
        productos = Producto.query.filter_by(activo=True).all()

    categorias = Categoria.query.all()
    return render_template('index.html', productos=productos, categorias=categorias, categoria_activa=categoria_id)

@main_bp.route('/producto/<string:sku>')
def detalle_producto(sku):
    producto = Producto.query.filter_by(sku=sku).first_or_404()
    return render_template('detalle.html', producto=producto)

@main_bp.route('/categorias')
def categorias():
    lista_categorias = Categoria.query.all()
    return render_template('categorias.html', categorias=lista_categorias)
