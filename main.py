from flask import Flask

app = Flask(__name__)

@app.route('/hello_world', methods=['GET'])
def call_func():
    import convertBits
    return convertBits.hello_world()

@app.route('/good_bye_world', methods=['GET'])
def call_func_2():
    import voltsToBin
    return voltsToBin.good_bye_world()


app.run(host="0.0.0.0")