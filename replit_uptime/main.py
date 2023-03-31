from flask import Flask
import requests

app = Flask('app')

#########################################
@app.route('/')
def hello_world():
  #return 'Hello, World!'

  badstatus = ''
  url = 'https://www.example.com'
  response = requests.get(url)
  status_code = response.status_code
  if status_code != 200:
    badstatus = badstatus+"; "+url

  if len(badstatus) != 0:
    return 'bad status: ' + badstatus

  return "ok"
###########################################


app.run(host='0.0.0.0', port=8080)
