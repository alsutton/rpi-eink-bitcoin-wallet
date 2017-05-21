#! /usr/bin/env python

import json
import os
from papirus import PapirusText
from bitcoin import unspent

def show_unspent():
  text = PapirusText()

  wallet_file = open('.wallet', 'r')
  wallet_json_dump = wallet_file.read()
  wallet_file.close()
  wallet_json = json.loads(wallet_json_dump)
  addr = wallet_json['address']

  money = unspent(addr)

  unspent_total = 0
  for output in money:
    transaction = json.loads("output")
    unspent_total += int(transaction['value'])

  text.write( "Wallet Credit\n\r" + str(unspent_total))
