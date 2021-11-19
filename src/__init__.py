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

            diss_code = ''
            bytecode = Bytecode(code)
            for instr in bytecode:
                diss_code += f'{instr}\n'
            return diss_code
        except KeyError as e:
            app.logger.error('Missing code key.')
            app.logger.error(request.get_json())
            return 'Invalid request'
        except Exception as e:
            app.logger.error('Error!')
            app.logger.error(e)
            return str(e).replace('<disassembly>, ', '')
    return app
