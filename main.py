from flask import Flask

import convertBits
import voltsToBin

app = Flask(__name__)

@app.route('/hello_world', methods=['GET'])
def call_func():
    return convertBits.hello_world()

@app.route('/good_bye_world', methods=['GET'])
def call_func_2():
    return voltsToBin.good_bye_world()


app.run(host="0.0.0.0", port="5002")