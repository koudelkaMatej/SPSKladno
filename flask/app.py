from flask import Flask, render_template, url_for, request, redirect, session
import os
import bcrypt
import mysql.connector
from pripojeni import *
app = Flask(__name__) # název před route

app.secret_key = 'Muj_tajny_klic'

@app.route('/')
def home():
    return "Ahoj, světe od učitele!"

@app.route('/1')
def pozdrav_returnem():
    return "Ahoj, světe od jedničky!"

@app.route('/2')
def pozdrav_ze_souboru():
    return render_template("index2.html")

@app.route('/3')
def pozdrav_ze_souboru_CSS():
    return render_template("index3.html")

@app.route('/4')
def pozdrav_z_promenny():
    text = "Ahoj z proměnné"
    return render_template("index4.html", message = text)

@app.route('/5') # Vložení obrázku do HTML z pythonu
def obrazek():
    image_url = url_for('static', filename='images/pan.png')  # cesta k obrázku
    #                         prvni je nazev v HTML druhý je název v pythonu
    return render_template('index5.html', image_url=image_url) 

<<<<<<< HEAD

if __name__ == "__main__":
    app.run()
=======
@app.route('/6', methods=['GET', 'POST']) # Předání formulářem z HTML do pythonu 
def prvniFormularCislo():
    result = None
    if request.method == 'POST':
        number = request.form.get('number', type=int) # přečti co je uložené v proměné number ze stránky HTML
        if number is not None:
            result = number + 1  # přičtení jedničky
    return render_template('index6.html', result=result)

#vytvoreni slozky, kam budu ukladat nahrane soubory
app.config["UPLOAD_FOLDER"] = "ukazkovyFlask/static/uploadedFiles/"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
@app.route('/7', methods=['GET', 'POST']) # Předání souboru
def deuhyFormFile():
    content = None
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename.endswith('.txt'):
            # Uložení souboru na disk
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)
            # Čtení obsahu souboru
            file.seek(0)  # Resetování pointeru souboru
            content = file.read().decode('utf-8')  # Přečti soubor jako text
    return render_template('index7.html', content=content)

import plotly.graph_objects as go
import plotly.io as pio
@app.route('/8')
def graph():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[10, 20, 25, 30], mode='lines+markers', name='Data 1'))
    fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[15, 18, 22, 27], mode='lines+markers', name='Data 2'))

    fig.update_layout(
        title="Ukázkový interaktivní graf",
        xaxis_title="X-osa",
        yaxis_title="Y-osa",
        template="plotly_white"
    )
    # Převod grafu do HTML
    graph_html = pio.to_html(fig, full_html=False)
    return render_template("index8.html", graph_html=graph_html)

@app.route('/8_2')
def graphBar():
    # Data
    fruit = ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"]
    contestant = ["Alex", "Alex", "Alex", "Jordan", "Jordan", "Jordan"]
    number_eaten = [2, 1, 3, 1, 3, 2]

    # Unikátní soutěžící
    unique_contestants = list(set(contestant))

    # Inicializace grafu
    fig = go.Figure()

    # Přidání stop pro každého soutěžícího
    for current_contestant in unique_contestants:
        # Filtrace dat pro aktuálního soutěžícího
        x = [fruit[i] for i in range(len(fruit)) if contestant[i] == current_contestant]
        y = [number_eaten[i] for i in range(len(number_eaten)) if contestant[i] == current_contestant]

        # Přidání stop
        fig.add_trace(go.Bar(
            x=x, 
            y=y, 
            name=current_contestant,
            hovertemplate=f"Contestant={current_contestant}<br>Fruit=%{{x}}<br>Number Eaten=%{{y}}<extra></extra>"
        ))

    # Nastavení layoutu
    fig.update_layout(
        legend_title_text="Contestant",
        title="Number of Fruits Eaten by Contestants",
    )
    fig.update_xaxes(title_text="Fruit")
    fig.update_yaxes(title_text="Number Eaten")

    # Převod grafu do HTML
    graph_html = pio.to_html(fig, full_html=False)
    return render_template("index8.html", graph_html=graph_html)

@app.route('/9/<int:id>/<string:name>',methods = ['GET']) # funkce update, která funguje tak, že napíšu do adresy ID řádku co hcic změnit, a poté na co
def parametry(id, name):
    return render_template("index9.html", id=id, name=name)

@app.route('/10', methods=['GET', 'POST']) # Předání formulářem z HTML do pythonu 
def redirekting():
    result = None
    if request.method == 'POST':
        number = request.form.get('number', type=int)
        result = number
        if number == 1:
            return redirect('/1')
        elif number == 2:
            return redirect('/2')
        else:
            return render_template("index10.html", result = result)
    else:
        return render_template("index10.html", result = result)
    

@app.route('/home')
def home_login_ukazka():
    # Hlavní stránka
    return render_template('home.html', email=session.get('email'))

@app.route('/logout')
def logout():
    # Odstranění uživatele ze session
    session.pop('email', None)
    return redirect(url_for('home_login_ukazka'))
@app.route('/register', methods=['GET', 'POST'])

def register():
    if request.method == 'POST':
        name = request.form['jmeno']
        mail = request.form['email']
        psw = request.form['psw']
        
        hashed_password = bcrypt.hashpw(psw.encode('utf-8'), bcrypt.gensalt())
        hesloDoDB = hashed_password.decode('utf-8')
        mydb = mysql.connector.connect(
        host = HOST
        ,user = USER
        ,password = PASSWORD
        ,database = DATABASE
        )
        
        mycursor = mydb.cursor()
        # Create the Pojišťovny table
        mycursor.execute("""CREATE TABLE IF NOT EXISTS uzivatele
        (
            id int AUTO_INCREMENT PRIMARY KEY,
            jmeno varchar(35) NOT NULL,
            email varchar(50) NOT NULL,
            heslo varchar(255) NOT NULL
        );""")
        mydb.commit()

        sql = "INSERT INTO uzivatele (jmeno, email, heslo) VALUES (%s, %s, %s)"
        values = (name, mail, hesloDoDB)
        mycursor.execute(sql, values)
        mydb.commit()

        return redirect(url_for('login'))
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']

        mydb = mysql.connector.connect(
            host = HOST
        ,user = USER
        ,password = PASSWORD
        ,database = DATABASE
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT heslo FROM uzivatele WHERE email = %s;", (email,))
        result = mycursor.fetchone()

        if result:
            stored_hashed_password = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
                session['email'] = email
                return redirect(url_for('home_login_ukazka'))
            else:
                error_message = "Invalid email or password."
        else:
            error_message = "User not found."

        return render_template("login.html", error=error_message)

    return render_template("login.html")

@app.route('/tabulka')
def tabulka():
    if 'email' not in session:
        # Pokud uživatel není přihlášený, přesměrujeme ho na login
        return redirect(url_for('login'))
    elif 'email' in session:
        mydb = mysql.connector.connect(
            host = HOST
            ,user = USER
            ,password = PASSWORD
            ,database = DATABASE
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM uzivatele")
        result = mycursor.fetchall()
        
        return render_template("tabulka.html", email=session.get('email'), items = result)

if __name__ == '__main__':
    app.run()
>>>>>>> f55ee4e5424a1506d697c2a7a0498b697706e49d
