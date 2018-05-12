import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/stock', methods=['POST'])
def stock():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))
    
    res = makeResponse(req)
    
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
	
def makeResponse(req):
	
	result = req.get("result")
	action = request.get("action")
	
	if x == 'stock.news':
		return getNewsDetails(req)
	elif x == 'stock.research':
		return getResearch(req)
	#if x in 'bc':
		# Fall-through by not using elif, but now the default case includes case 'a'!
	#elif x in 'xyz':
		# Do yet another thing
	else:
		return commonResponse("Sorry, I did't get you ?")
	
	
def getNewsDetails(req):

	# Request to get current news
	r=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=2e1b4cacd0694ac193f8e2659b82bed2')
    
	# Output response of news API
	json_object = r.json()
	
	dataSet=json_object['articles']
	temp = ""
	speech = "Today top new is : "
	
	for data in dataSet:
		title = data.get("title")
 		desc = data.get("description")
 		speech = title + ' ' + desc
 		temp = temp + speech
		
    return commonResponse(temp)

def getResearch(req)
	msg = "Today's fundamental research call. Buy Grasim Industries Limited. C M P rupees 1089. Target price Rupees 1300 with potential upside of 18 percent."
	return commonResponse(msg)
		
def commonResponse(msg):
	return {
			"speech":msg,
			"displayText":msg,		
			"source": "apiai-demostock-webhook"
	}
	
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
    
    
    
    
    