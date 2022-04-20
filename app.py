from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', pageTitle='VTM Site')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About Page')

def calculate_top_area(Radius)
    return 3.14*(radius**2)

def calculate_side_area(Radius,Height)
    return 2*(3.14*(radius*height))

def calculate_total_area_in(total_area_in)
    return side_area + top_area

def calculate_total_area_ft(total_sqft)
    return total_area/144

def calculate_material_cost(total_material_cost)
    return total_sqft * material_cost

def calculate_labor_cost(total_labor_cost)
    return labor_cost * total_sqft

def calculate_total_cost(cost)
    return total_material_cost +total_labor_cost

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        c_radius = float(form['radius'])
        height = float(form['height'])
        top_area=3.14*(radius**2)
        side_area=2*(3.14*(radius*height))
        total_area = top_area + side_area
        total_sqft = total_area/144
        material_cost = 25 
        total_material_cost = total_sqft*material_cost
        labor_cost = 15
        total_labor_cost = labor_cost*total_sqft
        cost = total_material_cost + total_labor_cost
        cost=str(cost)
        return cost
    return render_template('estimate.html', pageTitle="Estimate")
  
if __name__ == '__main__':
    app.run(debug=True)
