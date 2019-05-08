import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(host ="localhost",user ="root",database='hosp_db',passwd="xxx@555")
mycursor = mydb.cursor()

# mycursor.execute('CREATE TABLE Conditions( START DATETIME, STOP DATETIME, PATIENT VARCHAR(36), ENCOUNTER VARCHAR(36), CODE VARCHAR(36), DESCRIPTION TEXT,\
# FOREIGN KEY(PATIENT) REFERENCES Patient(PATIENT_ID), FOREIGN KEY(ENCOUNTER) REFERENCES Encounters(ENC_ID) \
# )')


df = pd.read_csv('./data/conditions.csv')

df = df[['START','STOP','PATIENT','ENCOUNTER','CODE','DESCRIPTION']]

row_str= ''
df = df.dropna()
for index,row in df.iterrows():
	new_str = []
	for col in df.columns:
		new_str.append(row[col])
	new_str =tuple(new_str)

	mycursor.execute('INSERT INTO conditions(START,STOP,PATIENT,ENCOUNTER,CODE,DESCRIPTION) VALUES(%s,%s,%s,%s,%s,%s)', new_str)
mydb.commit()



