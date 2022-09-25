from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions import db
from ..models.pd import Pd

pdBp = Blueprint('pdBp', __name__)

@pdBp.route('/db')
def create_db():
  #db.create_all()
  return "OIe"

@pdBp.route('/')
def pd_list():
  pds_query = Pd.query.all()
  return render_template('pd_list.html', pds=pds_query)
  # db.create_all()
  
@pdBp.route('/pd/create')
def create_pd():
  return render_template('pd_create.html')

@pdBp.route('/pd/add', methods=["POST"])
def add_pd():

    sNome = request.form["nome"]
    sPreco = request.form["tipo"]
    sQuantidade = request.form["inicio"]

    pd = Pd(nome=sNome, preco=sPreco, quantidade=sQuantidade)
    db.session.add(pd)
    db.session.commit()

    return redirect(url_for("pdBp.pd_list"))
  
@pdBp.route('/pd/update/<pd_id>')
def update_pd(pd_id=0):
    pds_query = Pd.query.filter_by(id = pd_id).first()
    return render_template('pd_update.html', pd=pds_query)
  
@pdBp.route('/pd/upd', methods=["POST"])
def upd_pd():

    iPd = request.form["id"]
    sNome = request.form["nome"]
    sPreco = request.form["preco"]
    dQuantidade = request.form["qtd"]

    pd = Pd.query.filter_by(id = iPd).first()
    pd.nome = sNome
    pd.preco = sPreco
    pd.quantidade = dQuantidade
    db.session.add(pd)
    db.session.commit()

    return redirect(url_for("pdBp.pd_list"))
  
@pdBp.route('/pd/delete/<pd_id>')
def delete_pd(pd_id=0):
    pd_query = Pd.query.filter_by(id = pd_id).first()
    return render_template('pd_delete.html', pd=pd_query)
  
@pdBp.route('/pd/dlt', methods=["POST"])
def dlt_pd():
  iPd = request.form["id"]
  pd = Pd.query.filter_by(id = iPd).first()
  db.session.delete(pd)
  db.session.commit()
  return redirect(url_for("pdBp.pd_list"))