from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from business.model_manager import ModelManager

app = Flask(__name__, static_folder='../client/pages')
CORS(app, supports_credentials=True)

@app.route("/get_food", methods=['POST'])
def get_food():
	data = request.json
	mm = ModelManager()
	try:

		food = mm.classify_image(data)
		print(food)

		data = {
			'message': 'OK',
			'food': food
			}
		resp = jsonify(data)
		return resp

	except Exception as e:
		data = {'message': e.args[0]}
		resp = jsonify(data)
		return resp

# Static file serving
@app.route('/')
def serve_index():
    return send_from_directory('../client/pages', 'home.html')

@app.route('/<path:path>')
def serve_static(path):
	if path.startswith('assets'):
		return send_from_directory('../client/assets', path[len('assets/'):])
	elif path.startswith('css'):
		return send_from_directory('../client/css', path[len('css/'):])
	elif path.startswith('scripts'):
		return send_from_directory('../client/scripts', path[len('scripts/'):])
	else:
		return send_from_directory('../client/pages', path)

if __name__ == "__main__":
	app.run(debug=True)