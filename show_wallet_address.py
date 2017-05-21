#! /usr/bin/env python

import os
import random
import string

from papirus import PapirusText
from bitcoin import *

def show_wallet_address():
  text = PapirusText()

  if not os.path.exists(".wallet"):
    priv = sha256(random.SystemRandom().choice(string.ascii_uppercase + string.digits))
    pub = privtopub(priv)
    addr = pubtoaddr(pub)
    wallet_json = {}
    wallet_json['private_key'] = priv
    wallet_json['address'] = addr
    wallet_json_dump = json.dumps(wallet_json)
    wallet_file = open('.wallet', 'w')
    wallet_file.write(wallet_json_dump)
    wallet_file.close
  else:
    wallet_file = open('.wallet', 'r')
    wallet_json_dump = wallet_file.read()
    wallet_file.close()
    wallet_json = json.loads(wallet_json_dump)
    addr = wallet_json['address']
    priv = wallet_json['private_key']

  split = -((-len(addr))//3)

  text.write(
	"Wallet Address\n" + 
	addr[:split] + "\n" + 
	addr[split:split*2] + "\n" + 
	addr[split*2:])

