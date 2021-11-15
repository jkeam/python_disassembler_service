from flask import Flask, jsonify, request
from flask_cors import CORS
from dis import Bytecode

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["*"])

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            return 'Welcome to the Python Disassembler Service'

        try:
            json_data = request.get_json()
            code = json_data['code']

            str = ''
            bytecode = Bytecode(code)
            for instr in bytecode:
                str += f'{instr}\n'
            return str
        except KeyError as e:
            print('Missing code key.')
            print(request.get_json())
            return ''
        except Exception as e:
            print('Error!')
            print(e)
            return ''

    return app
