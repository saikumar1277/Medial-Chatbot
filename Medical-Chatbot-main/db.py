from flask import Flask
from flask_mysqldb import MySQL
import csv
app = Flask(__name__)
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='12345678'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_DB']='MedicalChatbot'
mysql=MySQL(app)
@app.route('/')
def index():
    cur=mysql.connection.cursor()
    csv_data=csv.reader(open('symptom_Description.csv'))
    for r in csv_data:
        if r != ['Disease', 'Description']:
            r[0] = r[0].capitalize()
            r[1] = r[1].capitalize()
            r[1] = r[1].split(".")[0] + "."
            cur.execute('INSERT INTO description VALUES (%s,%s)',r)
    mysql.connection.commit()
    cur.close()
if __name__ == "__main__":
    app.run()
