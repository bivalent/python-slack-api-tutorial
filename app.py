import os
from slackclient import SlackClient

SLACK_TOKEN = 'token here'
CHANNEL = 'desired channel name here'

slack_client = SlackClient(SLACK_TOKEN)


def list_channels():
	channels_call = slack_client.api_call("channels.list")
	if channels_call.get('ok'):
		return channels_call['channels']
	return None


def channel_info(channel_id):
	channel_info = slack_client.api_call("channels.info", channel=channel_id)
	if channel_info:
		return channel_info['channel']
	return None


def send_message(channel_id, message):
	slack_client.api_call(
		"chat.postMessage",
		channel = channel_id,
		text = message,
		username = 'pythonbot',
		icon_emoji = ':robot_face:'
	)

def printFormattedMessage():
	response = ""
	row1 = ['USA', 'Delaware', '#1']
	row2 = ['USA', 'Pennsylvania', '#2']
	row3 = ['USA', 'New Jersey', '#3']
	row4 = ['USA', 'Georgia', '#4']
	row5 = ['USA', 'Conneticut', '#5']
	row6 = ['USA', 'Massechusetts', '#6']
	row7 = ['USA', 'Maryland', '#7']
	row8 = ['USA', 'Ohio', '#17']
	
	rowList = [row1, row2, row3, row4, row5, row6, row7, row8]
	
	for row in rowList:
		response += "\n{:12}{:25}{}".format(row[0], row[1], row[2])
		
	print(response)
	return response
	
if __name__ == '__main__':
	channels = list_channels()
	if channels:
		print("Channels: ")
		for c in channels:
			print(c['name'] + " (" + c['id'] + ")")
			channel_latest = channel_info(c['id'])

			if c['name'] == CHANNEL:
				send_message(c['id'], "This message sent from python code.")
				send_message(c['id'], printFormattedMessage())
		print('- - - - - -')
	else:
		print("Unable to authenticate.")
