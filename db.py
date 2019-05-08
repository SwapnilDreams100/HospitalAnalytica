import mysql.connector

from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api, reqparse
import argparse

app = Flask(__name__)

import pickle

CNXN = mysql.connector.connect(host ="localhost",user ="root",database='hosp_db',passwd="xxx@555")
CURSOR = CNXN.cursor()

@app.errorhandler(404)
def pageNotFound(error):
    return ("page not found")

@app.errorhandler(500)
def raiseError(error):
    return (error)

# count enc per year
@app.route('/q1', methods=['GET'])
def query1(): 

    global CNXN, CURSOR
    q1 = 'SELECT Count(enc_id), YEAR(Start) FROM Encounters GROUP BY Year(Start) order by year(start)'

    CURSOR.execute(q1)
    data = CURSOR.fetchall()

    new_data = []
    for i in data:
    	new_data.append({'label':i[1],'y':i[0]})
    return jsonify(new_data)

@app.route('/maps', methods=['GET'])
def query_maps(): 

    global CNXN, CURSOR
    q1 = 'SELECT latitude,longitude FROM organisation'

    CURSOR.execute(q1)
    data = CURSOR.fetchall()

    new_data = []
    for i in data:
    	new_data.append({'lat':i[0],'long':i[1]})
    return jsonify(new_data)

# max cost of a medication per year
@app.route('/q2', methods=['GET'])
def query2():
    
    global CNXN, CURSOR
    
    parser = reqparse.RequestParser()
    parser.add_argument('disease', type=str, required=True)
    args = parser.parse_args()
    
    DISEASE_NAME=args['disease']
    q2 ="SELECT MAX(Cost), Year(START) FROM cost_view where DESCRIPTION = %s GROUP BY YEAR(START) order by year(start)"
    CURSOR.execute(q2,(DISEASE_NAME,))
    
    data = CURSOR.fetchall()

    new_data = []
    for i in data:
    	new_data.append({'x':i[1],'y':float(i[0])})
    return jsonify(new_data)

# utilization per org
@app.route('/q3', methods=['GET'])
def query3(): 

    global CNXN, CURSOR
    q1 = 'SELECT Utilization, org_id FROM Organization'

    CURSOR.execute(q1)
    data = CURSOR.fetchall()

    new_data = []
    for i in data:
    	new_data.append({'y':float(i[0]), 'label':i[1]})
    return jsonify(new_data)

# get list of medications
@app.route('/q_medic', methods=['GET'])
def query_medic(): 

    global CNXN, CURSOR
    q1 = 'SELECT description FROM medications group by description'

    CURSOR.execute(q1)
    data = CURSOR.fetchall()
    return jsonify(data)

# get list of procedures
@app.route('/q_proc', methods=['GET'])
def query_proc(): 

    global CNXN, CURSOR
    q1 = 'SELECT description FROM procedures GROUP BY description'

    CURSOR.execute(q1)
    data = CURSOR.fetchall()
    return jsonify(data)

# max cost of a medication per year
@app.route('/q5', methods=['GET'])
def query5():
    
    global CNXN, CURSOR
    
    parser = reqparse.RequestParser()
    parser.add_argument('procedure', type=str, required=True)
    args = parser.parse_args()
    
    procedure_NAME=args['procedure']
    q5 ="SELECT MAX(Cost), Year(proc_DATE) FROM  procedures where DESCRIPTION = %s GROUP BY YEAR(proc_DATE) order by year(proc_date)"
    CURSOR.execute(q5,(procedure_NAME,))
    
    data = CURSOR.fetchall()

    new_data = []
    for i in data:
        new_data.append({'x':i[1],'y':float(i[0])})
    
    return jsonify(new_data)

@app.route('/q_cond', methods=['GET'])
def query_cond(): 

    global CNXN, CURSOR
    q1 = 'SELECT description FROM conditions GROUP BY description'

    CURSOR.execute(q1)
    data = CURSOR.fetchall()
    return jsonify(data)

@app.route('/q6', methods=['GET'])
def query6():
    
	global CNXN, CURSOR

	parser = reqparse.RequestParser()
	parser.add_argument('condition', type=str, required=True)
	args = parser.parse_args()

	cond_NAME=args['condition']
	q6 = 'select count(patient.gender)*100/(select count(*) from conditions where description=%s group by description )\
	from patient inner join conditions on conditions.patient=patient.PATIENT_ID where patient.gender=%s and conditions.description= %s group by conditions.description'

	CURSOR.execute(q6,(cond_NAME,'M',cond_NAME,))

	data = CURSOR.fetchall()

	new_data = []
	for i in data:
		new_data.append({'y':100.0-float(i[0]),'label':'F'})
		new_data.append({'y':float(i[0]),'label':'M'})
	
	return jsonify(new_data)

# get avg time of a disease
@app.route('/q4', methods=['GET'])
def query4():
    
    global CNXN, CURSOR
    q4 = 'SELECT (Avg(DATEDIFF(Stop,Start))),Description FROM Conditions GROUP BY Description'
    
    CURSOR.execute(q4)
    
    data = CURSOR.fetchall()

    new_data = []
    for i in data:
    	new_data.append({'label':i[1],'y':float(i[0])})
    	
    return jsonify(new_data)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return (response)

if __name__ == '__main__':
    app.run()