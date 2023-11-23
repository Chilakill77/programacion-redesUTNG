# Creando un servidor Web con Flask para proporcionar servicios
# mediante los métodos GET, PUT, DELETE, POST
# Profesor: Gabriel Barrón R.

import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crudr1.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET donde busca un nombre
@app.route('/', methods=['GET'])
def query_records():
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Animales, Cuidadores')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(registros)

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO Animales(id, nombre, especie, edad, color, fecha_nacimiento, tipo_alimentacion, habitat) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(insert, [record['id'], record['nombre'], record['especie'], record['edad'], record['color'], record['fecha_nacimiento'], record['tipo_alimentacion'], record['habitat']])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM Animales WHERE id= ?'
    cursor.execute(delete, [record['id']])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE Animales SET nombre = ? WHERE id= ?'
    cursor.execute(update, [record['nombre'], record['id']])
    conn.commit()
    return jsonify(record)

if __name__ == '__main__':
    app.run(debug=True)
