
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
    cursor.execute('SELECT * FROM Cuidadores')
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
    insert = 'INSERT INTO Cuidadores(id, nombre, edad, correo, direccion, telefono, fecha_contratacion, tipo_empleado, id_animal) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(insert, [record['id'], record['nombre'], record['edad'], record['correo'], record['direccion'], record['telefono'], record['fecha_contratacion'], record['tipo_empleado'], record['id_animal']])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM Cuidadores WHERE id= ?'
    cursor.execute(delete, [record['id']])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE Cuidadores SET nombre = ? WHERE id= ?'
    cursor.execute(update, [record['nombre'], record['id']])
    conn.commit()
    return jsonify(record)

if __name__ == '__main__':
    app.run(debug=True)
