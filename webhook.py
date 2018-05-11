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
	
def makeResponse(res):
	#result = res.get("result");
	speech = "This is news."
	#return {
	#"speech":speech,
	#"displayText":speech,
	#"source":"apiai-demostock-webhook"
	#}
	
	#return {
	#	"fulfillmentText": speech,
	#	"fulfillmentMessages": [
	#		{
	#			"speech":speech
	#		}
	#	]
	#}
	
	#return {
	#		"fulfillmentText": "This is a text response",
	#		"fulfillmentMessages": [
	#		  {
	#			"card": {
	#			  "title": "card title",
	#			  "subtitle": "card text",
	#			  "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
	#			  "buttons": [
	#				{
	#				  "text": "button text",
	#				  "postback": "https://assistant.google.com/"
	#				}
	#			  ]
	#			}
	#		  }
	#		],
	#		"source": "example.com",
	#		"payload": {
	#		  "google": {
	#			"expectUserResponse": "true",
	#			"richResponse": {
	#			  "items": [
	#				{
	#				  "simpleResponse": {
	#					"textToSpeech": "this is a simple response"
	#				  }
	#				}
	#			  ]
	#			}
	#		  },
	#		  "facebook": {
	#			"text": "Hello, Facebook!"
	#		  },
	#		  "slack": {
	#			"text": "This is a text response for Slack."
	#		  }
	#		},
	#		"outputContexts": [
	#		  {
	#			"name": "projects/${PROJECT_ID}/agent/sessions/${SESSION_ID}/contexts/context name",
	#			"lifespanCount": "5",
	#			"parameters": {
	#			  "param": "param value"
	#			}
	#		  }
	#		],
	#		"followupEventInput": {
	#		  "name": "event name",
	#		  "languageCode": "en-US",
	#		  "parameters": {
	#			"param": "param value"
	#		  }
	#		}
	#	}
	#
	
	return {
		"speech": "this text is spoken out loud if the platform supports voice interactions",
		"displayText": "this text is displayed visually",
		"messages": {
		  "type": 1,
		  "title": "card title",
		  "subtitle": "card text",
		  "imageUrl": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png"
		},
		"data": {
		  "google": {
			"expectUserResponse": "true",
			"richResponse": {
			  "items": [
				{
				  "simpleResponse": {
					"textToSpeech": "this is a simple response"
				  }
				}
			  ]
			}
		  },
		  "facebook": {
			"text": "Hello, Facebook!"
		  },
		  "slack": {
			"text": "This is a text response for Slack."
		  }
		},
		"contextOut": [
		  {
			"name": "context name",
			"lifespan": "5",
			"parameters": {
			  "param": "param value"
			}
		  }
		],
		"source": "example.com",
		"followupEvent": {
		  "name": "event name",
		  "parameters": {
			"param": "param value"
		  }
		}
	}
	
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
