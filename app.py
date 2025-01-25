import os
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection using environment variables
db = mysql.connector.connect(
    host=os.getenv('DB_HOST', 'sql.mwhepworth.me'),
    user=os.getenv('DB_USER', 'todo'),
    password=os.getenv('DB_PASSWORD', 'CSE310ToDoListApp#'),
    database=os.getenv('DB_NAME', 'recipie')
)

@app.route('/', methods=['GET', 'HEAD'])
def home():
    if request.method == 'HEAD':
        return '', 200  # Return only headers
    cursor = db.cursor()
    cursor.execute("SELECT id, recipe_name FROM new_table ORDER BY recipe_name")
    recipes = cursor.fetchall()
    cursor.close()
    return render_template('form.html', recipes=recipes)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    food_type = request.form.get('food_type', 'default_value')  # Set default value if not provided
   
    cursor = db.cursor()
    cursor.execute("INSERT INTO new_table (recipe_name, food_type) VALUES (%s, %s)", (name, food_type))
    db.commit()
    cursor.close()

    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    recipe_id = request.form['id']
    cursor = db.cursor()
    cursor.execute("DELETE FROM new_table WHERE id = %s", (recipe_id,))
    db.commit()
    cursor.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)