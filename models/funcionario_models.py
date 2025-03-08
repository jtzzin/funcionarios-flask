from db import db
 
class Funcionario(db.Model):
    __tablename__ = 'funcionarios'
 
    id= db.Column(db.Integer, primary_key=True)
    nome= db.Column(db.String(100), nullable= False)
    cargo= db.Column(db.String(100), nullable=False)
    salario= db.Column(db.Float, nullable=False)
    
    
    def json(self):
        return {
            'id': self.id,          
            'nome': self.nome,    
            'cargo': self.cargo,
            'salario': self.salario
        }