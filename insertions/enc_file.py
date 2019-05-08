import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(host ="localhost",user ="root",database='hosp_db',passwd="xxx@555")
mycursor = mydb.cursor()


#	PRIMARY KEY(ENC_ID), FOREIGN KEY(PATIENT) REFERENCES PATIENT(PATIENT_ID), FOREIGN KEY(ORGANIZATION) REFERENCES ORGANIZATION(ORG_ID))')

df = pd.read_csv('./data/encounters.csv')

df = df[['ID', 'START' , 'PATIENT', 'PROVIDER', 'ENCOUNTERCLASS','CODE', 'DESCRIPTION']]
df['START']=df['START'].apply(lambda x: (x.split('T')[0]))
row_str= ''
print(df.head())
df=df.dropna()
for index,row in df.iterrows():
	new_str = []
	for col in df.columns:
		new_str.append(row[col])
	new_str =tuple(new_str)
	
	mycursor.execute('INSERT INTO Encounters(ENC_ID, START,PATIENT,ORGANIZATION,ENCOUNTER_CLASS,CODE,DESCRIPTION) VALUES(%s,%s,%s,%s,%s,%s,%s)', new_str)
mydb.commit()

