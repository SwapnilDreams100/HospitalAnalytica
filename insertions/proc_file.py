import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(host ="localhost",user ="root",database='hosp_db',passwd="xxx@555")
mycursor = mydb.cursor()

# mycursor.execute('CREATE TABLE Procedures( PROC_DATE DATETIME,PATIENT VARCHAR(36),ENCOUNTER VARCHAR(36),CODE VARCHAR(36),DESCRIPTION TEXT,COST VARCHAR(36), \
# FOREIGN KEY(PATIENT) REFERENCES Patient(PATIENT_ID), FOREIGN KEY(ENCOUNTER) REFERENCES Encounters(ENC_ID) \
	# )')

df = pd.read_csv('data/procedures.csv')

df = df[['DATE','PATIENT','ENCOUNTER','CODE','DESCRIPTION','COST']]

row_str= ''

for index,row in df.iterrows():
	new_str = []
	for col in df.columns:
		new_str.append(row[col])
	new_str =tuple(new_str)

	mycursor.execute('INSERT INTO procedures(PROC_DATE,PATIENT,ENCOUNTER,CODE,DESCRIPTION,COST) VALUES(%s,%s,%s,%s,%s,%s)', new_str)
mydb.commit()