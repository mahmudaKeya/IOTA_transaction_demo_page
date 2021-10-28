import iota_client
import os
import hashlib

import subprocess as s
#s.Popen('C:\\Users\\User\\AppData\\Local\\Programs\\desktop\\Firefly.exe')


client = iota_client.Client()
print(client.get_info())


IOTA_SEED_SECRET = os.getenv('IOTA_SEED_SECRET')

if not IOTA_SEED_SECRET:
    raise Exception("Please define environment variable called `IOTA_SEED_SECRET`")
'''
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Encrypt') == 'Encrypt':
            # pass
            print("Encrypted")
        elif  request.form.get('Decrypt') == 'Decrypt':
            # pass # do something else
            print("Decrypted")
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
            # return render_template("index.html")
        print("No Post Back Call")
        return render_template("index.html")
    
    
    if __name__ == '__main__':
        app.run()
'''