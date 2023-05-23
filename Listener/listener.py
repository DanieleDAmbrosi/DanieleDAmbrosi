from flask import Flask, request
import json

app = Flask(__name__)

file = open("dump.txt", 'ab')

@app.route('/', methods=['GET', 'POST'])
def root():
  print("data: ", request.data)
  file.write(request.data)
  file.flush()
  return ''

app.run()