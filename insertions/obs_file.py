import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(host ="localhost",user ="root",database='hosp_db',passwd="xxx@555")
mycursor = mydb.cursor()
 #mycursor.execute('CREATE TABLE Observations( OBS_DATE DATETIME,PATIENT VARCHAR(36),ENCOUNTER VARCHAR(36),CODE VARCHAR(36), DESCRIPTION TEXT, VALUE VARCHAR(36),UNITS VARCHAR(36),FOREIGN KEY(PATIENT) REFERENCES Patient(PATIENT_ID), FOREIGN KEY(ENCOUNTER) REFERENCES Encounters(ENC_ID) \
#)')


df = pd.read_csv('./data/observations.csv')

df = df[['DATE','PATIENT','ENCOUNTER','CODE','DESCRIPTION','VALUE','UNITS']]

row_str= ''
df = df.dropna()
for index,row in df.iterrows():
	new_str = []
	for col in df.columns:
		new_str.append(row[col])
	new_str =tuple(new_str)

	mycursor.execute('INSERT INTO Observations(OBS_DATE,PATIENT,ENCOUNTER,CODE,DESCRIPTION,VALUE,UNITS) VALUES(%s,%s,%s,%s,%s,%s,%s)', new_str)
mydb.commit()
