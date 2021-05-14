import sys
sys.path.append("./banco.py")
from banco import *
import os
import requests
import random
from flask import Flask, Response, request, render_template, redirect
from pynput.keyboard import Key, Controller

keyboard = Controller()        
app = Flask(__name__)

bd = Banco()

# CRUD para usuários, números e planos (assinatura?)


@app.route("/")
def index():
    bd.showMessage()
    return render_template("test.html", name="askdjkajhsdj"), 200

@app.route("/opa", methods=['POST'])
def show_values():
    if request.method == 'POST':
        print(request.form['idade'])
        print(request.form['id'])

    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    return render_template('index_api.html'), 200


#  Create, Read, Update & Delete


# ----- Routes for Users -------
# Read
@app.route("/users", methods=['GET'])
def users_index():
    users = bd.getAllUsers()
    return render_template('users/index.html', users = users), 200
@app.route("/users/<id>", methods=['GET'])
def users_show(id):
    user = bd.getUser(id)
    return render_template('users/show.html', user = user), 200

# Create User
@app.route("/users/new", methods=['GET'])
def users_new():
    return render_template('users/new.html'), 200
@app.route("/users/create", methods=['POST'])
def users_create():
    # Receber dados
    nome = request.form['nome']
    email = request.form['email']
    cpf = request.form['cpf']

    # Validar dados: 

    user = (nome, email, cpf)
    result = bd.createNewUser(user)
    

    if(result):
        # Deu tudo certo!
        return redirect(f"/users")
    else:
        # Algo deu errado...
        return render_template(), 400


# Update
@app.route("/users/edit/<id>", methods=['GET'])
def users_edit(id):
    user = bd.getUser(id)
    return render_template("users/edit.html", user=user)
@app.route("/users/update", methods=['POST'])
def users_update():
    # Receber dados
    id = request.form['id']
    nome = request.form['nome']
    email = request.form['email']
    cpf = request.form['cpf']

    # Validar dados: 

    user = (id, nome, email, cpf)
    result = bd.updateUser(user)
    

    if(result):
        # Deu tudo certo!
        return redirect(f"/users")
    else:
        # Algo deu errado...
        return render_template(), 400

# Delete
@app.route("/users/delete/<id>", methods=['GET'])
def users_delete(id):
    # Validar dados: 

    result = bd.deleteUser(id)

    if(result):
        # Deu tudo certo!
        return redirect(f"/users")
    else:
        # Algo deu errado...
        return render_template(), 400

# ----- END Routes for Users -------





# ----- Routes for Numbers -------

# Read
@app.route("/numbers", methods=['GET'])
def numbers_index():
    numbers = bd.getAllNumbers()
    return render_template('numbers/index.html', numbers = numbers), 200
@app.route("/numbers/<id>", methods=['GET'])
def numbers_show(id):
    number = bd.getNumber(id)
    print(number)
    user = bd.getUser(number[1])
    ddd = bd.getDDD(number[2])
    ddi = bd.getDDI(number[3])
    chip = bd.getChip(number[4])
    return render_template('numbers/show.html', numero = number[5], user = user[1], ddd = ddd[1], ddi = ddi[1], disponivel = chip[4]), 200

# Create User
@app.route("/numbers/new", methods=['GET'])
def numbers_new():
    users = bd.getAllUsers()
    operadoras = bd.getAllOperadoras()
    ddds = bd.getAllDDDs()
    ddis = bd.getAllDDIs()
    data = (ddis, ddds, operadoras, users)
    return render_template('numbers/new.html', data = data), 200
@app.route("/numbers/create", methods=['POST'])
def numbers_create():
    # Receber dados

    user_id = request.form['user_id']
    ddi_id = request.form['ddi_id']
    ddd_id = request.form['ddd_id']
    operadora_id = request.form['operadora_id']
    number = request.form['number']
    
    chip = random.choice(bd.getAllChipsFromOperadora(operadora_id))

    # Validar dados: 

    numero = (user_id, ddd_id, ddi_id, chip[0], number)

    result = bd.createNewNumber(numero)
    bd.updateChip(chip)

    if(result):
        # Deu tudo certo!
        return redirect(f"/numbers")
    else:
        # Algo deu errado...
        return render_template(), 400

# Update
@app.route("/numbers/edit/<id>", methods=['GET'])
def numbers_edit(id):
    number = bd.getNumber(id)
    users = bd.getAllUsers()
    operadoras = bd.getAllOperadoras()
    chip = bd.getChip(number[4])
    operadora = bd.getOperadora(chip[1])
    ddds = bd.getAllDDDs()
    ddis = bd.getAllDDIs()
    data = (users, operadoras, ddds, ddis)
    return render_template("numbers/edit.html", data = data, number = number, numberOperadora = operadora)
@app.route("/numbers/update", methods=['POST'])
def numbers_update():
    # Receber dados
    id = request.form['id']
    number = bd.getNumber(id)

    user_id = request.form['user_id']
    ddi_id = request.form['ddi_id']
    ddd_id = request.form['ddd_id']
    operadora_id = request.form['operadora_id']
    numero = request.form['number']
    chip = bd.getChip(number[4])
    if(chip[1] != operadora_id):
        ops = bd.getAllChipsFromOperadora(operadora_id)
        print("operadoras from chips:")
        print(operadora_id)
        print(ops)
        newChip = random.choice(ops)
        toUpdate = (chip[0], chip[1], chip[2], chip[3], 1)
        bd.updateChip(toUpdate)
        chip = newChip
        toUpdate = (chip[0], chip[1], chip[2], chip[3], 0)
        bd.updateChip(toUpdate)

    
    # Validar dados: 

    updatedNumber = (id, user_id, ddd_id, ddi_id, chip[0], numero)
    result = bd.updateNumber(updatedNumber)

    if(result):
        # Deu tudo certo!
        return redirect(f"/numbers")
    else:
        # Algo deu errado...
        return render_template(), 400

# Delete
@app.route("/numbers/delete/<id>", methods=['GET'])
def numbers_delete(id):
    # Validar dados: 

    result = bd.deleteUser(id)

    if(result):
        # Deu tudo certo!
        return redirect(f"/numbers")
    else:
        # Algo deu errado...
        return render_template(), 400

# ----- END Routes for Numbers -------

if  __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")