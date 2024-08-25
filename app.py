#!/usr/bin/env python3

import argparse
from flask import Flask, send_from_directory, abort

app = Flask(__name__)

# Whitelisted files
whitelisted_files = {
	'index.html',
	'script.js'
}

@app.route('/')
def serve_index():
	return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static_files(filename):
	if filename in whitelisted_files:
		return send_from_directory('.', filename)
	else:
		abort(404)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Simple File Server')
	parser.add_argument('-p', '--port', type=int, default=8812, help='Port to run the server on (default: 8812)')
	args = parser.parse_args()
	app.run(port=args.port, debug=True)

