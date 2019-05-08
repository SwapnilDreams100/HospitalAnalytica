import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(host ="localhost",user ="root",database='hosp_db',passwd="xxx@555")
mycursor = mydb.cursor()

#mycursor.execute("drop table Medications;")
#mycursor.execute("CREATE TABLE Medications( START DATETIME, STOP DATETIME, PATIENT VARCHAR(36), ENCOUNTER VARCHAR(36), DESCRIPTION TEXT, CODE int(10), COST DEC , FOREIGN KEY(PATIENT) REFERENCES patient(PATIENT_ID), FOREIGN KEY(ENCOUNTER) REFERENCES encounters(ENC_ID));")

#mycursor.execute('CREATE TABLE Organization(ORG_ID VARCHAR(36), NAME TEXT, ADDRESS TEXT ,CITY TEXT ,STATE TEXT, UTILIZATION VARCHAR(36),PRIMARY KEY(ORG_ID) )')

df = pd.read_csv('./data/medications.csv')

df = df[['START','STOP','PATIENT','ENCOUNTER','CODE','DESCRIPTION','COST']]

row_str= ''

for index,row in df.iterrows():
	new_str = []
	for col in df.columns:
		if str(row[col]) == "nan":
			new_str.append("0000-00-00")
		else:
			new_str.append(row[col])
	new_str =tuple(new_str)
	mycursor.execute('INSERT INTO Medications(START,STOP,PATIENT,ENCOUNTER,CODE,DESCRIPTION,COST) VALUES(%s,%s,%s,%s,%s,%s,%s)', new_str)

mydb.commit()

