from slackclient import SlackClient
import urllib.request
url="https://google.pl/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req, timeout=3)
redirected = res.geturl() != url

if redirected == 1:
    message = "Filmu jeszcze nie ma!"
else:
    message = "Jest film już jest!"

def slack_message(message, channel):
    token = '<TOKEN>'
    sc = SlackClient(token)
    sc.api_call('chat.postMessage', channel=channel,
                text=message, username='My Sweet Bot',
                icon_emoji=':robot_face:')

slack_message(message,"general")
