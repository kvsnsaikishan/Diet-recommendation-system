from flask import Flask, render_template, request
from algo import calc_tdee, generate_diet_plan

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        name = request.form['name']
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = int(request.form['age'])
        gender = request.form['gender']
        phys_act = request.form['phys_act']
        diet_plan = request.form['diet_plan']

        tdee = calc_tdee(name, weight, height, age, gender, phys_act)
        diet = generate_diet_plan(tdee, diet_plan)

        return render_template('result.html', name=name, diet=diet)

if __name__ == '__main__':
    app.run(debug=True)
