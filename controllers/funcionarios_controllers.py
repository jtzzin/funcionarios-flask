from models.funcionario_models import Funcionario
from db import db
import json
from flask import make_response

def get_funcionarios():
    funcionarios= Funcionario.query.all()
    
    if not funcionarios:
        response = make_response(
            json.dumps({
                'mensagem':'nenhum funcionario encontrado',
                'dados': []
            },ensure_ascii=False,sort_keys=False)
        )
    else:
        response = make_response(
            json.dumps({
                'mensagem':'Lista de funcionarios',
                'dados': [funcionario.json() for funcionario in funcionarios]
            },ensure_ascii=False,sort_keys=False)
        )
    response.headers['Content-Type'] = 'application/json'
    return response


def get_funcionario_by_id(funcionario_id):
    funcionario = Funcionario.query.get(funcionario_id)
        
    if funcionario:
        response = make_response(
            json.dumps({
                'mensagem':'Funcionario econtradp',
                'dados': funcionario.json()
            },ensure_ascii, sort_keys=False)
        )
        response.headers['Content-Type'] ='application/json'
        return response
    else:
        response = make_response(
            json.dumps({
                'mensagem':'Funcionario não encontrado',
                'dados':{}
            },ensure_ascii=False), 
            404 
        )
        response.headers['Content-Type'] ='application/json'
        return response
        
        
def get_funcionario_by_nome(funcionario_nome):
    funcionario = Funcionario.query.filter_by(nome=funcionario_nome).first() # busca o primeiro
   
    if funcionario:
        response = make_response(
            json.dumps({
                'mensagem':'funcionario encontrado',
                'dados': funcionario.json()
            },sort_keys=False)
        )
        response.headers['Content-Type'] ='application/json'
        return response
    else:
        response = make_response(
            json.dumps({
                'mensagem':'funcionario não encontrado',
                'dados':{}
            },sort_keys=False)
        )
        response.headers['Content-Type'] ='application/json'
        return response, 404
    

def create_funcionario(funcionario_data):
 if not all(key in funcionario_data for key in ['nome','cargo','salario']):
        response = make_response(
            json.dumps({'mensagem': 'Dados invalidos.Nome,cargo e salário obrigatórios.'},ensure_ascii=False),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    
    novo_funcionario = Funcionario(
        nome =funcionario_data['nome'],    
        cargo = funcionario_data['cargo'],
        salario = funcionario_data['salario']        
    )
    
    db.session.add(novo_funcionario)
    db.session.commit()
    
    response = make_response(
        json.dumps({  
            'mensagem': 'Funcionário cadastrado com sucesso.',  
            'funcionario': novo_funcionario.json()  
        },ensure_ascii=False, sort_keys=False)  
    )
    response.headers['Content-Type'] = 'application/json'
    return response

def update_funcionario(funcionario_id,funcionario_data):
    funcionario = Funcionario.query.get(funcionario_id)
 
    if not funcionario:
        response = make_response(
            json.dumps({'Mensagem':'Funcionário não encontrado'}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response
   
    if not all(key in funcionario_data for key in ['nome','cargo','salario']):
        response = make_response(
            json.dumps({'mensagem': 'dados inválidos.Nome,cargo,salario são obrigatórios'},ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response
   
    funcionario.nome = funcionario_data['nome']
    funcionario.cargo= funcionario_data['cargo']
    funcionario.salario = funcionario_data['salario']
 
    db.session.commit()
 
    response = make_response(
        json.dumps({
            'mensagem':'Funcionário atualizado com sucesso.',
            'funcionario': funcionario.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response

def delete_funcionario(funcionario_id):
    funcionario = Funcionario.query.get(funcionario_id)
    if not funcionario:
        response = make_response(
            json.dumps({
                'mensagem': 'Funcionário não encontrado'
            }, ensure_ascii=False),
            404  
        )
        response.header['Content-Type'] = 'application/json'
        return response
    
    db.session.delete(funcionario)
    db.session.commit()
    
    response = make_response(
        json.dumps({
            'mensagem': 'Funcionário excluido com sucesso'
        }, ensure_ascii=False,sort_keys=False)
    )
    response.header['Content-Type'] = 'application/json'
    return response
    
    