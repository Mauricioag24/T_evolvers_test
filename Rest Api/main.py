from flask import Flask, render_template, request, jsonify, redirect, url_for
from elasticsearch import Elasticsearch
from uuid import uuid4
import querys
import methods
import time
es = Elasticsearch([{'host': 'localhost', 'port':9200}])
app = Flask(__name__)
@app.route("/")
def hi():
    # es.indices.delete(index='t_evolvers_test')
    if es.indices.exists(index='t_evolvers_test'):
        return redirect(url_for('inicio'))
    else:
        es.indices.create(index='t_evolvers_test', body=querys.mappings())
        print ("Index created")
    return redirect(url_for('inicio'))


@app.route('/data', methods=['POST', 'GET'])
def data():
    """Show the information about the booking and allow to do the payment

    :return: Booking information
    :rtype: string
    """
    time.sleep(1)
    result = es.search(index='t_evolvers_test', body=querys.search(ide))
    data = methods.send_data(result)
    if request.method=='POST':
        form_name=request.form['button']
        if form_name == 'Cerrar Sesion':
            return redirect(url_for('inicio'))
        if form_name == 'Regresar':
            return redirect(url_for('booking'))
        if form_name == 'Pagar':
            es.update(index='t_evolvers_test', id = ide, body=querys.update_pay())
            return render_template('inicio.html', msg= "Successful payment")
    return render_template('data.html', data=data)


@app.route('/info', methods=['POST','GET'])
def info():
    """Show the information about the booking and allow to do the payment, Also can update the existing booking

    :return: Booking information
    :rtype: string
    """
    global ide
    result=es.search(index='t_evolvers_test', body=querys.search_book(token, usr))
    data = methods.send_data(result)
    ide = result['hits']['hits'][0]['_id'] 
    if token != data[2]:
        error = "Invalid Token"
        return render_template('reserva.html', error=error)
    if request.method=='POST':
        form_name=request.form['button']
        if form_name=='Cerrar Sesion':
            return redirect(url_for('inicio'))
        if form_name=='Regresar':
            return redirect(url_for('reserva'))
        if form_name == 'Editar Reserva':
            ide = result['hits']['hits'][0]['_id']
            return redirect(url_for('booking'))
        if form_name == 'Pagar':
            es.update(index='t_evolvers_test', id = ide, body=querys.update_pay())
            return render_template('inicio.html', msg= "Successful payment") 
    return render_template('info.html', data=data)


@app.route('/reserva', methods=['POST','GET'])
def reserva():
    """Login with user and booking token

    :return: app route 
    :rtype: template
    """
    global usr, token
    if request.method=='POST':
        form_name = request.form['button']
        if form_name == 'Ingresar':
            usr = request.form.get('usr')
            token = request.form.get('tkn')
            return redirect(url_for('info'))
        if form_name == 'Regresar':
            return redirect(url_for('inicio'))
    return render_template('reserva.html')


@app.route('/booking', methods=['POST', 'GET'])
def booking():
    """Create new booking

    :return: App route
    :rtype: Template
    """
    if request.method=='POST':
        form_name=request.form['button']
        if form_name == 'Ingresar':
            checkin = request.form.get('chi')
            checkout = request.form.get('cho')
            add = request.form.get('add')
            token = uuid4().hex[:6] 
            es.update(index='t_evolvers_test', id = ide, body=querys.update(token, checkin, checkout, add))
            return redirect(url_for('data'))
        if form_name == 'Regresar':
            return redirect('login')
        if form_name == 'Actualizar':
            checkin = request.form.get('chi')
            checkout = request.form.get('cho')
            es.update(index='t_evolvers_test', id = ide, body=querys.update_dates(checkin, checkout))
            return redirect(url_for('data'))
    return render_template('booking.html')
    

@app.route("/create_user", methods=['POST', 'GET'])
def create_user():
    """Create new users in database

    :return: Succesful index and App route
    :rtype: template
    """
    if request.method=='POST':
        form_name = request.form['button']
        if form_name =='Ingresar':
            rand_token = uuid4().hex[:6]
            name = request.form.get('nm')
            lastn = request.form.get('ln')
            es.index(index='t_evolvers_test', document= querys.insert_data(name, lastn, usr, pssd), id = rand_token)
            return render_template('login.html', msg= "Successful index")       
        if form_name=='Regresar':
            return redirect(url_for('inicio'))
    return render_template('create_user.html')


@app.route("/search")
def search():
    """Search user data storage in database

    :return: Redirect to create_user or booking
    :rtype: template
    """
    global ide
    result = es.search(index='t_evolvers_test', body=querys.search_user(usr, pssd))
    value = result['hits']['total']['value']
    if value == 0:
        return redirect(url_for('create_user'))
    else: 
        ide = result['hits']['hits'][0]['_id']
        return redirect(url_for('booking'))


@app.route("/login", methods=['POST','GET'])
def login():
    """Login with user and password

    :return: search the user data
    :rtype: url
    """
    global usr, pssd
    if request.method=='POST':
        # form_name= request.form['button']
        usr = request.form.get('usr')
        pssd = request.form.get('pssd')
        return redirect(url_for('search'))
    return render_template('login.html')


@app.route('/inicio', methods=['POST', 'GET'])
def inicio():
    if request.method=='POST':
        form_name=request.form['button']
        if form_name=='Nueva Reserva':
            return redirect(url_for('login'))
        if form_name=='Ya Tengo Reserva':
            return redirect(url_for('reserva'))
    return render_template('inicio.html')

if __name__ == '__main__':
    app.run('localhost', debug=True)