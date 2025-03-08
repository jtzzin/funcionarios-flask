from flask import Blueprint, request  
from controllers.funcionarios_controllers import(
    get_funcionarios,
    get_funcionario_by_id,
    get_funcionario_by_nome,
    create_funcionario,
    update_funcionario,
    delete_funcionario
)
 
funcionario_routes = Blueprint('funcionario_routes', __name__)  
 
@funcionario_routes.route('/Funcionarios', methods=['GET'])
def funcionario_get():
    return get_funcionarios()
 
@funcionario_routes.route('/Funcionario/<int:funcionario_id>', methods =['GET'])
def funcionario_get_by_id(funcionario_id):
    return get_funcionario_by_id(funcionario_id)
 
@funcionario_routes.route('/Funcionario/<string:funcionario_nome>', methods=['GET'])
def funcionario_get_by_nome(funcionario_nome):
   return get_funcionario_by_nome(funcionario_nome)


@funcionario_routes.route('/Funcionnario/', methods = ['POST'])
def funcionarios_post():
    return create_funcionario(request.json)

@funcionario_routes.route('/Funcionario/<int:funcionario_id>', methods = ['PUT'])
def funcionario_put(funcionario_id):
    return update_funcionario(funcionario_id):

@funcionario_routes.route('/Funcionario/<int:funcionario_id>', methods = ['DELETE'])
def funcionario_delete(funcionario_id):
    return delete_funcionario(funcionario_id):


 