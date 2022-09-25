from ..extensions import db

class Pd(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    preco = db.Column(db.String(50))
    quantidade = db.Column(db.String(10))

    def __repr__(self):
        return "<Pd(nome={}, preco={}, quantidade={})>".format(self.nome, self.preco, self.quantidade)