from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        value_soup = 2
        value_salad = 3
        value_coffee = 2
        value_water = 1
        num_soup = request.form['soup']
        num_salad = request.form['salad']
        num_coffee = request.form['coffee']
        num_water = request.form['water']
        total_soup = int(num_soup)*value_soup
        total_salad = int(num_salad)*value_salad
        total_coffee = int(num_coffee)*value_coffee
        total_water = int(num_water)*value_water
        
        final_result = total_soup + total_salad + total_coffee + total_water 
        return render_template('index.html', href2='soup='+num_soup+', salad='+num_salad+', coffee='+num_coffee+', water='+num_water+', Total = '+str(final_result))
      
