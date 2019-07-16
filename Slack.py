###A Message Sent To Slack Using Python Code
##import requests
##import json
##web_hook_url="https://hooks.slack.com/services/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"
##
##slack_msg= {"text" : "Welcome to the DevOps Channel!"}
##
##requests.post(web_hook_url,data=json.dumps(slack_msg))



#SLACKBOT SENDS MESSAGE INTO SLACK USING PYTHON CODE

import sys
from slacker import Slacker
slack= Slacker("xoxb-688071234149-688750368052-tM8wyl3b1eIzENpiK9jnsR9y")
#Send a message to #techwork channel
message= "Hello Everyone! Welcome to the #random Channel"
slack.chat.post_message('#random', message);
