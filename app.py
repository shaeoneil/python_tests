from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', pageTitle='VTM Site')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About Page')

def calculate_top_area(radius):
    return 3.14*(radius**2)

def calculate_side_area(radius,height):
    return 2*(3.14*(radius*height))


@app.route('/estimate', methods=['GET','POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        pi = 3.14
        top_area = pi * radius**2
        side_area = 2*(pi*(radius*height))
        total_area = topArea+sidesArea
        total_sqft = totalArea / 144
        total_material_cost = 25 * totalSqFt
        total_labor_cost = 15 * totalSqFt
        cost = "${:,.2f}".format(round(total_material_cost + total_labor_cost, 2))
        return (render_template('estimate.html', estimate = cost))
    return render_template('estimate.html', pageTitle='Estimate')

if __name__ == '__main__':
    app.run(debug=True)
