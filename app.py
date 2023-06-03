from flask import Flask
import json
import dbhelpers
app = Flask(__name__)

@app.get('/cars')
def get_cars():
    results = dbhelpers.run_procedure('call get_all_cars()', [])
    cars_json = json.dumps(results, default=str)
    return cars_json

app.run(debug=True)