from logging import debug
from flask import Flask, redirect, url_for, render_template
import flask

import iota_client
import os
import hashlib

#flask import 
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/payment_iota", methods=["POST", "GET"])
def payment_iota():
    print("Transaction ongoing!")
    return render_template("payment_iota.html")

#if __name__ == "__main__":
#    app.run(debug=True)

import subprocess as s
s.Popen('C:\\Users\\User\\AppData\\Local\\Programs\\desktop\\Firefly.exe')

if __name__ == "__main__":
    app.run(debug=True)




client = iota_client.Client()
print(client.get_info())


IOTA_SEED_SECRET = os.getenv('IOTA_SEED_SECRET')

if not IOTA_SEED_SECRET:
    raise Exception("Please define environment variable called `IOTA_SEED_SECRET`")

client = iota_client.Client()

a = (int) (client.get_balance(seed=IOTA_SEED_SECRET))


address_changed_list = client.get_addresses(
    seed=IOTA_SEED_SECRET,
    account_index=0,
    input_range_begin=0,
    input_range_end=10,
    get_all=True
)
print(address_changed_list)

print("Return a balance for a single address:")


print(
    client.get_address_balance("atoi1qp460yty766mqdkhs3yy70rqj5zn2dzr9gs4yzhzhvdaayva4ach5crvzhp")
)


print("Return a balance for the given seed and account_index:")

print(
    client.get_balance(
        seed=IOTA_SEED_SECRET,
        account_index=0,
        initial_address_index=0
    )
)


print("for a", a)



while True:
    b = (int)(client.get_balance(seed=IOTA_SEED_SECRET))
    print("Please wait!, Transaction is in process....")
    if (b>a):
        print("Congratulation!! Your Transaction is successful")
        #clean
        break




