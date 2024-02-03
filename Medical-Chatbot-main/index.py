from flask import Flask, request, render_template, session, redirect
from twilio.rest import Client
from flask_session import Session
import random
from promise import Promise
import tensorflow as tf
import numpy as np
from flask_mysqldb import MySQL
import hmac
import hashlib
import base64
from datetime import date
app = Flask(__name__)
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='12345678'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_DB']='MedicalChatbot'
account_sid = "AC0beb072ebbc1f71ccfa9a535cc464125"
auth_token = "e1be943eeba696aefc3982083874e687"
client = Client(account_sid, auth_token)
mysql=MySQL(app)
user_name = ''
user_mobilenumber = ''
user_age = None
@app.route('/')
def index():
    session["user"] = None
    return render_template('index.html', check="0")
@app.route("/register")
def register():
    return render_template('register.html')
@app.route("/verify", methods=["POST"])
def verify():
    session["user"] = request.form
    string = str(random.randint(0, 9))
    string += str(random.randint(0, 9))
    string += str(random.randint(0, 9))
    string += str(random.randint(0, 9))
    mobile_number = request.form["mobile_number"]
    client.messages.create("+91" + str(mobile_number), from_="+12512766639",
                           body="OTP for Medical Chatbot registration is " + string)
    session["otp"] = string
    return render_template("verify.html", number=mobile_number, check="0")
@app.route("/verification", methods=["POST"])
def verification():
    if session["user"] is None or session["otp"] is None:
        return redirect("/")
    string = request.form["1"]
    string += request.form["2"]
    string += request.form["3"]
    string += request.form["4"]
    if string == session["otp"]:
        return redirect("/details")
    else:
        return render_template("verify.html", number=session["user"]["mobile_number"], check="1")
@app.route("/details")
def details():
    name = session["user"]["name"]
    mobilenumber = session["user"]["mobile_number"]
    password = session["user"]["password"]
    age = session["user"]["age"]
    password = hmac.new(bytes("12345678", "UTF-8"), msg=bytes(password, "UTF-8"), digestmod=hashlib.sha256).digest()
    password = base64.b64encode(password).decode()
    cur=mysql.connection.cursor()
    cur.execute("insert into users values(%s, %s, %s, %s);", [name, mobilenumber, password, int(age)])
    mysql.connection.commit()
    cur.close()
    session["otp"] = None
    session["user"] = None
    return render_template('index.html', check="1")
@app.route("/login", methods=["POST"])
def login():
    mobilenumber = request.form["mobile_number"]
    password = request.form["password"]
    password = hmac.new(bytes("12345678", "UTF-8"), msg=bytes(password, "UTF-8"), digestmod=hashlib.sha256).digest()
    password = base64.b64encode(password).decode()
    cur=mysql.connection.cursor()
    cur.execute("select name, mobilenumber, age from users where mobilenumber = %s and password = %s", [mobilenumber, password])
    data = list(cur.fetchall())
    mysql.connection.commit()
    cur.close()
    if len(data) == 0:
        return render_template('index.html', check="2")
    else:
        global user_name
        user_name = str(list(data[0])[0])
        global user_mobilenumber
        user_mobilenumber = str(list(data[0])[1])
        global user_age
        user_age = int(list(data[0])[2])
        cur=mysql.connection.cursor()
        cur.execute("select * from medicalhistory where mobilenumber = %s;", [mobilenumber])
        medicalhistory = list(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        if len(medicalhistory) != 0:
            for i in range(len(medicalhistory)):
                medicalhistory[i] = list(medicalhistory[i])
                for k in medicalhistory[i][4].split("\n"):
                    medicalhistory[i].append(k)
        return render_template('login.html', user_name = user_name, medicalhistory = medicalhistory)
@app.route("/signout")
def signout():
    global user_name
    user_name = ''
    global user_mobilenumber
    user_mobilenumber = ''
    global user_age
    user_age = None
    return redirect("/")
@app.route('/dialogflow', methods=['POST'])
def dialogflow():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = ''
    query_result = req.get('queryResult')
    if query_result.get('action') == 'input.welcome':
        return { "fulfillmentMessages": [
                {
                "text": {
                    "text": [
                        "Hello! " + user_name
                    ]
                    }
                },
                {
                "text": {
                    "text": [
                        "How can I help you?"
                    ]
                    }
                }]}
    elif query_result.get('action') == 'Symptom':
        return {"fulfillmentText": 'Enter the symptoms\nFor example "High fever, Sweating, Headache"'}
    elif query_result.get('action') == 'Symptom.Symptom-custom':
        symptom = query_result.get('parameters').get('symptoms').split(",")
        output = Promise(lambda resolve, reject: resolve(predict(symptom)))
        if output.get() == "Invalid symptoms":
            return {"fulfillmentText": "Not able to predict, kindly consult doctor.\nThank you!"}
        else:
            description = "Description: "
            for i in output.get().split("+")[3].split("?"):
                description += i
            j = 1
            precaution = "Precautions:\n"
            for i in output.get().split("+")[4].split("?"):
                precaution += str(j) + ") " + i + ".\n"
                j += 1
            return { "fulfillmentMessages": [
                {
                "text": {
                    "text": [
                        "Predicted disease: " + output.get().split("+")[0]
                    ]
                    }
                },
                {
                "text": {
                    "text": [
                        "This is a " + output.get().split("+")[1] + "."
                    ]
                    }
                },
                {
                "text": {
                    "text": [
                        description
                    ]
                    }
                },
                {
                "text": {
                    "text": [
                        precaution
                    ]
                    }
                },
                {
                "text": {
                    "text": [
                        "Consult doctor:\n" + output.get().split("+")[2]
                    ]
                    }
                }]}
def predict(symptom):
    symptoms_input = []
    symptoms = ['itching', 'skin rash', 'nodal skin eruptions', 'continuous sneezing', 'shivering', 'chills', 'joint pain', 'stomach pain', 'acidity', 'ulcers on tongue', 'muscle wasting', 'vomiting', 'burning micturition', 'spotting  urination', 'fatigue', 'weight gain', 'anxiety', 'cold hands and feets', 'mood swings', 'weight loss', 'restlessness', 'lethargy', 'patches in throat', 'irregular sugar level', 'cough', 'high fever', 'sunken eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish skin', 'dark urine', 'nausea', 'loss of appetite', 'pain behind the eyes', 'back pain', 'constipation', 'abdominal pain', 'diarrhoea', 'mild fever', 'yellow urine', 'yellowing of eyes', 'acute liver failure', 'fluid overload', 'swelling of stomach', 'swelled lymph nodes', 'malaise', 'blurred and distorted vision', 'phlegm', 'throat irritation', 'redness of eyes', 'sinus pressure', 'runny nose', 'congestion', 'chest pain', 'weakness in limbs', 'fast heart rate', 'pain during bowel movements', 'pain in anal region', 'bloody stool', 'irritation in anus', 'neck pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen legs', 'swollen blood vessels', 'puffy face and eyes', 'enlarged thyroid', 'brittle nails', 'swollen extremeties', 'excessive hunger', 'extra marital contacts', 'drying and tingling lips', 'slurred speech', 'knee pain', 'hip joint pain', 'muscle weakness', 'stiff neck', 'swelling joints', 'movement stiffness', 'spinning movements', 'loss of balance', 'unsteadiness', 'weakness of one body side', 'loss of smell', 'bladder discomfort', 'foul smell of urine', 'continuous feel of urine', 'passage of gases', 'internal itching', 'toxic look (typhos)', 'depression', 'irritability', 'muscle pain', 'altered sensorium', 'red spots over body', 'belly pain', 'abnormal menstruation', 'dischromic  patches', 'watering from eyes', 'increased appetite', 'polyuria', 'family history', 'mucoid sputum', 'rusty sputum', 'lack of concentration', 'visual disturbances', 'receiving blood transfusion', 'receiving unsterile injections', 'coma', 'stomach bleeding', 'distention of abdomen', 'history of alcohol consumption', 'fluid overload.1', 'blood in sputum', 'prominent veins on calf', 'palpitations', 'painful walking', 'pus filled pimples', 'blackheads', 'scurring', 'skin peeling', 'silver like dusting', 'small dents in nails', 'inflammatory nails', 'blister', 'red sore around nose', 'yellow crust ooze']
    for j in symptom:
        if len(j) <= 3:
            continue
        for i in symptoms:
            if j.strip().lower() in i:
                symptoms_input.append(i)
                break
    if len(symptoms_input) == 0:
        return "Invalid symptoms"
    x_input = [0] * len(symptoms)
    for i in symptoms_input:
        x_input[symptoms.index(i)] = 1
    labels = ['Migraine', 'GERD', 'Pneumonia', '(vertigo) Paroymsal  Positional Vertigo', 'Heart attack', 'Impetigo', 'Fungal infection', 'Osteoarthristis', 'Hypoglycemia', 'Tuberculosis', 'Malaria', 'Diabetes', 'Urinary tract infection', 'Arthritis', 'Hypertension', 'Allergy', 'Peptic ulcer diseae', 'Hypothyroidism', 'Chicken pox', 'Varicose veins', 'Dengue', 'Jaundice', 'Dimorphic hemmorhoids(piles)', 'Hepatitis B', 'Chronic cholestasis', 'Acne', 'Common Cold', 'Hepatitis C', 'Cervical spondylosis', 'Hepatitis D', 'Bronchial Asthma', 'Hyperthyroidism', 'Typhoid', 'Hepatitis E', 'Psoriasis', 'hepatitis A', 'Paralysis (brain hemorrhage)', 'Gastroenteritis']
    model = tf.keras.models.load_model('my_model.h5')
    probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    x_input = np.array([x_input])
    y_input = probability_model.predict(x_input)
    predicted_disease = labels[np.argmax(y_input[0])]
    Rheumatologist = ['Osteoarthristis','Arthritis']
    Cardiologist = ['Heart attack','Bronchial Asthma','Hypertension ']
    ENT_specialist = ['(vertigo) Paroymsal  Positional Vertigo','Hypothyroidism']
    Neurologist = ['Varicose veins','Paralysis (brain hemorrhage)','Migraine','Cervical spondylosis']
    Allergist_Immunologist = ['Allergy','Pneumonia','Common Cold','Tuberculosis','Malaria','Dengue','Typhoid']
    Urologist = ['Urinary tract infection','Dimorphic hemmorhoids(piles)']
    Dermatologist = ['Acne','Chicken pox','Fungal infection','Psoriasis','Impetigo']
    Gastroenterologist = ['Peptic ulcer diseae', 'GERD','Chronic cholestasis','Gastroenteritis','Hepatitis E','Jaundice','hepatitis A','Hepatitis B', 'Hepatitis C', 'Hepatitis D','Diabetes ','Hypoglycemia']
    if predicted_disease in Rheumatologist :
       consultdoctor = "Dr. Sarvajeet Pal\nRheumatologist\nhttps://www.practo.com/hyderabad/doctor/sarvajeet-pal-rheumatologist?practice_id=1054846&specialization=Rheumatologist&referrer=doctor_listing"
    elif predicted_disease in Cardiologist :
       consultdoctor = "Dr. Gokul Reddy\nCardiologist\nhttps://www.practo.com/hyderabad/doctor/dr-gokul-reddy-m-cardiologist?practice_id=1054846&specialization=Cardiologist&referrer=doctor_listing"
    elif predicted_disease in ENT_specialist :
       consultdoctor = "Dr. Sampurna Ghosh\nENT specialist\nhttps://www.practo.com/hyderabad/doctor/sampurna-ghosh-ear-nose-throat-ent-specialist?practice_id=1154495&specialization=Ear-nose-throat%20(ent)%20specialist&referrer=doctor_listing"
    elif predicted_disease in Neurologist :
       consultdoctor = "Dr. S Srikanth Reddy\nNeurologist\nhttps://www.practo.com/hyderabad/doctor/s-srikanth-reddy-neurosurgeon?practice_id=1154495&specialization=Neurologist&referrer=doctor_listing"
    elif predicted_disease in Allergist_Immunologist :
       consultdoctor = "Dr. Vyakarnam Nageshwar\nAllergist/Immunologist\nhttps://www.practo.com/hyderabad/doctor/viyakarnam-nageshwar-allergist-immunologist?practice_id=893315&specialization=Allergist/immunologist&referrer=doctor_listing"
    elif predicted_disease in Urologist :
       consultdoctor = "Dr. M Gopichand\nUrologist\nhttps://www.practo.com/hyderabad/doctor/dr-m-gopichand-urologist?practice_id=1357464&specialization=Urologist&referrer=doctor_listing"
    elif predicted_disease in Dermatologist :
       consultdoctor = "Dr. Soumya Podduturi\nDermatologist\nhttps://www.practo.com/hyderabad/doctor/drsoumya-21-yahoo-co-in-dermatologist-cosmetologist-general-physician?practice_id=1333468&specialization=Dermatologist&referrer=doctor_listing"
    elif predicted_disease in Gastroenterologist :
       consultdoctor = "Dr. Gabriel Sukumar Chinnam\nGastroenterologist\nhttps://www.practo.com/hyderabad/doctor/dr-sukumar-chinnam-gastroenterologist?practice_id=1357627&specialization=Gastroenterologist&referrer=doctor_listing"
    else :
       consultdoctor = "Other"
    major = ['Malaria', 'hepatitis A', 'Hypoglycemia', 'Diabetes', 'Hypertension', 'Peptic ulcer diseae', 'Cervical spondylosis', 'Urinary tract infection', 'Paralysis (brain hemorrhage)', 'Typhoid', 'Hepatitis B', 'Hepatitis C', 'Hepatitis E', 'Dengue', 'Hepatitis D', 'Heart attack', 'Pneumonia', 'Tuberculosis']
    minor = ['Allergy', 'Hypothyroidism', 'Psoriasis', 'GERD', 'Chronic cholestasis', 'Osteoarthristis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Impetigo', 'Dimorphic hemmorhoids(piles)', 'Common Cold', 'Chicken pox', 'Hyperthyroidism', 'Varicose veins', 'Fungal infection', 'Migraine', 'Bronchial Asthma', 'Jaundice', 'Arthritis', 'Gastroenteritis']
    disease = ""
    if predicted_disease in major:
        disease = "major disease"
    else:
        disease = "minor disease"
    cur=mysql.connection.cursor()
    cur.execute("select * from description where disease = %s;", [predicted_disease])
    description = list(cur.fetchall()[0])[1:]
    cur.execute("select * from precaution where disease = %s;", [predicted_disease])
    precaution = list(cur.fetchall()[0])[1:]
    if '' in precaution:
        precaution.remove("")
    mysql.connection.commit()
    cur.close()
    cur=mysql.connection.cursor()
    for i in range(len(symptoms_input)):
        symptoms_input[i] = symptoms_input[i].capitalize()
    cur.execute("insert into medicalhistory values(%s, %s, %s, %s, %s);", [user_mobilenumber, str(date.today()), ", ".join(symptoms_input), predicted_disease, consultdoctor])
    mysql.connection.commit()
    cur.close()
    output = predicted_disease + "+" + disease + "+" + consultdoctor + "+" + "?".join(description) + "+" + "?".join(precaution)
    return output
if __name__ == "__main__":
    app.config["SESSION_PERMANENT"] = True
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    app.run(port = 1000, debug = True)
