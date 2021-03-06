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
	action = result.get("action")
	
	if action == 'stock.news':
		return getNewsDetails(req)
	elif action == 'stock.research':
		return getResearch(req)
	if action in 'action.Login':
		return getLoginService(req)
	if action in 'input.welcome':
		return getUsername(req)
		# Fall-through by not using elif, but now the default case includes case 'a'!
	#elif action in 'xyz':
		# Do yet another thing
	else:
		return commonResponse("Sorry, I did't get you ?")
	
	
def getNewsDetails(req):

	# Request to get current news
	r=requests.get('')
    
	# Output response of news API
	json_object = r.json()
	
	dataSet=json_object['articles']
	temp = ""
	speech = "Today top new is : "
	
	for data in dataSet:
		title = data["title"]
		desc=data['description']
		speech = title + " " + desc
		break
		#temp = temp + speech
		
	return commonResponse(speech)
	
def getUsername(req):
	
	accessToken = "Bearer " + req['originalRequest']['data']['user']['accessToken']
	
	print(accessToken)
	
	# Add your url
	url = ""

	headers = {
		'authorization': accessToken,
		'cache-control': "no-cache",
		'postman-token': "83689df6-f3e3-30bb-a2de-ed30d1211721"
		}

	response = requests.request("GET", url, headers=headers)
	print(response.text)
	obj = response.json()
	msg = "Hi " + obj['name'] + ", Welcome to demo!"
	return commonResponse(msg)
	
	
def getLoginService(req):

	username = req['result']['parameters']['username']
	password = req['result']['parameters']['password']
	id = 0

	# Add your url
	url = ""

	payload = {
				"emailId": username,
				"password": password
			}
			
	payload = json.dumps(payload, indent=4)
				
	headers = {
		'content-type': "application/json"
		}

	response = requests.request("POST", url, data=payload, headers=headers)

	print(response.text)

	obj = response.json()
	
	if obj['responseCode'] == 1:
		id = obj['id']
		temp = 'Thank you user : ' + str(obj['id'])
	else:
		temp = obj['responseMessage']

	return commonSessionResponse(temp, id, 'test-context')


def getResearch(req):
		msg="Today's fundamental research call. Buy Grasim Industries Limited. C M P rupees 1089. Target price Rupees 1300 with potential upside of 18 percent."
		return commonResponse(msg)
		
def commonResponse(msg):
	return {
			"speech":msg,
			"displayText":msg,
			"source": "apiai-demostock-webhook"
	}
	
def commonSessionResponse(msg, id, contextName):
	return {
			"speech":msg,
			"displayText":msg,
			"source": "apiai-demostock-webhook",
			"contextOut":[
				{
					"name" : contextName,
					"lifespan": 99,
					"parameters" : {
						"id" : id
					}
				}
			]
	}
	
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
    
    
    
    
    