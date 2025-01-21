from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Phatsaxman1*",
#     database="family_recipe"
# )
db = mysql.connector.connect(
    host="sql.mwhepworth.me",
    user="todo",
    password="CSE310ToDoListApp#",
    database="recipie"
)

@app.route('/')
def form():
    cursor = db.cursor()
    cursor.execute("SELECT id, recipe_name FROM new_table")
    recipes = cursor.fetchall()
    cursor.close()
    return render_template('form.html', recipes=recipes)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
   
    cursor = db.cursor()
    cursor.execute("INSERT INTO new_table (recipe_name) VALUES (%s)", (name,))
    db.commit()
    cursor.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)