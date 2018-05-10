import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in globle layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
	req = request.get_json(slient=True, force=True)
	print(json.dumps(req, indent=4))
	
	res = makeResponse(req)
	res = json.dumps(res, indent=4)
	r = make_response(res)
	r.headers['Content-Type'] = "application/json"
	return req
	
def makeResponse(res):
	result = res.get('result');
	speech = "This is news."
	return {
	"speech": speech,
	"displayText": speech,
	"source": "apiai-demostock-webhook"
	}
	
if __name__ == '__main__':
	port = int(os.getenv('PORT', 5000))
	print("Start app on port " % port)
	app.run(debug=False, port=port, host='0.0.0.0')
