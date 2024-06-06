from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    cnpj = db.Column(db.String(20))

    def __repr__(self):
        return f'<User {self.id}>'
    
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    price = db.Column(db.String(20))

    def __repr__(self):
        return f'<Produto {self.id}>'

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = Users(name=data['name'], cnpj=data['cnpj'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuário criado'}), 201

@app.route('/user', methods=['GET'])
def get_users():
    users = Users.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'cnpj': user.cnpj} for user in users])

@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    user = Users.query.get(id)
    if not user:
        return jsonify({'message': 'Usuario não encontrado'}), 404
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.cnpj = data.get('cnpj', user.cnpj)
    db.session.commit()
    return jsonify({'message': 'Usuário atualizado'})

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = Users.query.get(id)
    if not user:
        return jsonify({'message': 'Usuário não encontrado'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Usuário deletado'})

@app.route('/produto', methods=['POST'])
def create_produto():
    data = request.get_json()
    new_produto = Produto(nome=data['nome'], price=data['price'])
    db.session.add(new_produto)
    db.session.commit()
    return jsonify({'message': 'Produto criado'}), 201


@app.route('/produto/<int:id>', methods=['GET'])
def get_produto_by_id(id):
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({'message': 'Produto não existe'}), 404
    return jsonify({
        'id': produto.id,
        'nome': produto.nome,
        'price': produto.price
    })

@app.route('/produto', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    if not produtos:
        return jsonify({'message': 'produto não encontrado'}), 404
    return jsonify([{
        'id': produto.id,
        'nome': produto.nome,
        'price': produto.price
    } for produto in produtos])


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
