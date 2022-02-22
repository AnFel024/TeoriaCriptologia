from flask import Flask, jsonify
from flask import request

import ast

app = Flask(__name__)
global formula

@app.route('/hello_world', methods=['GET'])
def call_func():
    import convertBits
    return convertBits.hello_world("")

@app.route('/codificar', methods=['POST'])
def code_func():
    import convertBits
    if request.method == 'POST':
        language = request.get_data().decode()
        chain = ast.literal_eval(language)
        print(chain)

    response = jsonify({'volts': convertBits.hello_world(chain["binary_chain"])})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/good_bye_world', methods=['GET'])
def call_func_2():
    import voltsToBin
    return voltsToBin.good_bye_world("")

@app.route('/decodificar', methods=['POST'])
def call_decodificar():
    import voltsToBin
    language = request.get_data().decode()
    volts = ast.literal_eval(language)
    print(volts)
    response = jsonify({'bin_chain': voltsToBin.good_bye_world(volts["volts_chain"])})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


app.run(host="0.0.0.0")