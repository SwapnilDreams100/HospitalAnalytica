import mysql.connector
import pandas as pd
import uszipcode
search = uszipcode.SearchEngine(simple_zipcode=True)

mydb = mysql.connector.connect(host ="localhost",user ="root",database='hosp_db',passwd="xxx@555")
mycursor = mydb.cursor()

#mycursor.execute('CREATE TABLE Condition( Start DATETIME, STOP DATETIME, PATIENT VARCHAR(36), ENCOUNTER VARCHAR(36), CODE STRING, DESCRIPTION STRING, \
# 	FOREIGN KEY(PATIENT) REFERENCES Patient(PATIENT_ID), FOREIGN KEY(ENCOUNTER) REFERENCES Encounter(ENCOUNTER_ID) \
# 	)')


#mycursor.execute('CREATE TABLE Organisation(ORG_ID VARCHAR(36), NAME TEXT, ADDRESS TEXT ,CITY TEXT ,STATE TEXT, UTILIZATION VARCHAR(36),Latitude VARCHAR(10),Longitude varchar(10),PRIMARY KEY(ORG_ID) )')

df = pd.read_csv('./data/organizations.csv')

df = df[['ID', 'NAME','ADDRESS','CITY','STATE','UTILIZATION','ZIP']]

row_str= ''

for index,row in df.iterrows():
	new_str = []
	for col in df.columns:
		if col =='ZIP':
			zipcode = search.by_zipcode(str(row[col]))
			latitute = (zipcode.to_dict()['lat'])
			longitude = zipcode.to_dict()['lng']
			new_str.append(latitute)
			new_str.append(longitude)
		else:
			new_str.append(row[col])
	new_str =tuple(new_str)

	mycursor.execute('INSERT INTO Organisation(ORG_ID, NAME,ADDRESS,CITY,STATE,UTILIZATION,latitude,longitude) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)', new_str)
mydb.commit()

