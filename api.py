import sys

from flask.helpers import url_for
sys.path.append("./banco.py")
from banco import *
import os
import requests
import random
from flask import Flask, Response, request, render_template, redirect
from werkzeug.utils import secure_filename
from pynput.keyboard import Key, Controller

UPLOAD_FOLDER = "/uploads/images"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

bd = Banco()

# CRUD para usuários, números e planos (assinatura?)


@app.route("/")
def index():
    return render_template("index_api.html"), 200

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

    filename = "image_"+str(user[0])+".png"
    print(type(user[4]))
    with open("static/image_"+filename, 'wb') as f:
        f.write(user[4])
    
    return render_template('users/show.html', user = user, filename = filename), 200

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
    file = request.files['profile'].read()
    print(file)

    # Validar dados: 

    user = (nome, email, cpf, file)
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
    i = 0
    for number in numbers:
        chip = bd.getChip(number[4])
        operadora = bd.getOperadora(chip[1])
        numbers[i] = number + (operadora[1],)
        i += 1
    print(numbers)
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
    
    availableChips = bd.getAllChipsFromOperadora(operadora_id)
    if(not availableChips):
        print("n tem mais chips")
        return "Não há mais Chips disponíveis para esta operadora<br><a href='/numbers/new'>Voltar</>", 400
    
    chip = random.choice(availableChips)

    # Validar dados: 

    numero = (user_id, ddd_id, ddi_id, chip[0], number)
    
    bd.updateChip(chip, 0)

    result = bd.createNewNumber(numero)

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
        newChip = random.choice(ops)
        toUpdate = (chip[0], chip[1], chip[2], chip[3], 1)
        bd.updateChip(toUpdate, 1)
        chip = newChip
        toUpdate = (chip[0], chip[1], chip[2], chip[3], 0)
        bd.updateChip(toUpdate, 0)

    
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

    result = bd.deleteNumber(id)

    if(result):
        # Deu tudo certo!
        return redirect(f"/numbers")
    else:
        # Algo deu errado...
        return render_template(), 400

# ----- END Routes for Numbers -------




# ----- Routes for Plans -------

# Read
@app.route("/plans", methods=['GET'])
def plans_index():
    plans = bd.getAllPlans()
    i = 0
    for plan in plans:
        agency = bd.getAgency(plan[1])
        plans[i] = plan + (agency[2],)
        i += 1
    print(plans)
    return render_template('plans/index.html', plans = plans), 200
@app.route("/plans/<id>", methods=['GET'])
def plans_show(id):
    plan = bd.getPlan(id)
    print(plan)
    agency = bd.getAgency(plan[1])
    return render_template('plans/show.html', plan = plan, agency = agency[2]), 200

# Create User
@app.route("/plans/new", methods=['GET'])
def plans_new():
    agencies = bd.getAllAgencies()
    return render_template('plans/new.html', agencies = agencies), 200

@app.route("/plans/create", methods=['POST'])
def plans_create():
    # Receber dados

    agency_id = request.form['agency_id']
    name = request.form['name']
    price = request.form['price']
    expire_date = request.form['expire_date']
  
    # Validar dados: 

    plano = (agency_id, name, price, 0, expire_date)

    result = bd.createNewPlan(plano)

    if(result):
        # Deu tudo certo!
        return redirect(f"/plans")
    else:
        # Algo deu errado...
        return render_template(), 400

# Update
@app.route("/plans/edit/<id>", methods=['GET'])
def plans_edit(id):
    plan = bd.getPlan(id)
    agencies = bd.getAllAgencies()
    agency = bd.getAgency(plan[1])
    return render_template("plans/edit.html", plan = plan, agencies = agencies, planAgency = agency[0])
@app.route("/plans/update", methods=['POST'])
def plans_update():
    id = request.form['id']
    agency_id = request.form['agency_id']
    name = request.form['name']
    price = request.form['price']
    expire_date = request.form['expire_date']
    
    # Validar dados: 

    updatedPlan = (id, agency_id, name, price, 0, expire_date)
    result = bd.updatePlan(updatedPlan)

    if(result):
        # Deu tudo certo!
        return redirect(f"/plans")
    else:
        # Algo deu errado...
        return render_template(), 400

# Delete
@app.route("/plans/delete/<id>", methods=['GET'])
def plans_delete(id):
    # Validar dados: 

    result = bd.deletePlan(id)

    if(result):
        # Deu tudo certo!
        return redirect(f"/plans")
    else:
        # Algo deu errado...
        return render_template(), 400

# ----- END Routes for plans -------



if  __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")