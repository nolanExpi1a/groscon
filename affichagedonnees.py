from flask import Flask, render_template, request, redirect
import pymysql
app = Flask(__name__)

# Configuration de la connexion à la base de données MySQL
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='basededonneesfestival')

@app.route('/')
def afficher_donnees():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM t_todolist_calendrier")
    data = cursor.fetchall()
    return render_template('index.html', data=data)


@app.route('/ajouter', methods=['POST'])
def ajouter_donnees():
    titre = request.form['titre']
    description = request.form['description']

    cursor = connection.cursor()
    cursor.execute("INSERT INTO t_todolist_calendrier (titre, description) VALUES (%s, %s)", (titre, description))
    connection.commit()

    return render_template('InsertPage.html')

if __name__ == '__main__':
    app.run()