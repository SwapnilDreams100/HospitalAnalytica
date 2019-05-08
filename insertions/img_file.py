import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(host ="localhost",user ="root",database='hosp_db',passwd="xxx@555")
mycursor = mydb.cursor()

# mycursor.execute('CREATE TABLE Imaging_studies(IMG_DATE DATETIME, ID varchar(36), PATIENT VARCHAR(36), ENCOUNTER VARCHAR(36), MODALITY_CODE VARCHAR(36), MODALITY_DESCRIPTION TEXT,SOP_CODE VARCHAR(36),SOP_DESCRIPTION TEXT,\
#  	FOREIGN KEY(PATIENT) REFERENCES Patient(PATIENT_ID), FOREIGN KEY(ENCOUNTER) REFERENCES Encounters(ENC_ID) \
#  )')


df = pd.read_csv('./data/imaging_studies.csv')

df = df[['DATE','ID','PATIENT','ENCOUNTER','MODALITY_CODE','MODALITY_DESCRIPTION','SOP_CODE','SOP_DESCRIPTION']]

row_str= ''
df = df.dropna()
for index,row in df.iterrows():
	new_str = []
	for col in df.columns:
		new_str.append(row[col])
	new_str =tuple(new_str)

	mycursor.execute('INSERT INTO imaging_studies(IMG_DATE,ID,PATIENT,ENCOUNTER,MODALITY_CODE,MODALITY_DESCRIPTION,SOP_CODE,SOP_DESCRIPTION) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)', new_str)
mydb.commit()



