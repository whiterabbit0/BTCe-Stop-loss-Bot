#! python3
# Donate if you want/can 
# BTC: 1CqwtF5w2UsFk7tKkREFuHT4NEophxj8JC
# LTC: Lh8bnJXpTq42YXRDm9V4DUvMT5AmNAttDL
import configparser
import http.client
import urllib
import urllib.request
import json
import code
import sys
import os.path
import time
import BTCe

api = BTCe.API('BTCe.ini')

def btc_usd_query():
	response = json.loads(urllib.request.urlopen('https://btc-e.com/api/2/btc_usd/ticker').read().decode('utf-8'))
	return response	
def ltc_usd_query():
	response = json.loads(urllib.request.urlopen('https://btc-e.com/api/2/ltc_usd/ticker').read().decode('utf-8'))
	return response	
def ltc_btc_query():
	response = json.loads(urllib.request.urlopen('https://btc-e.com/api/2/ltc_btc/ticker').read().decode('utf-8'))
	return response	
	

pair = input('What currency pair would you like to use? \n 1: BTC/USD \n 2: LTC/USD \n 3: LTC/BTC \n ')


if pair == '1' :
	pair = 'BTC_USD'
	selling = 'BTC'
	fore = 'USD'
	strpair = 'BTC/USD'
	ticker = btc_usd_query()
	ticker = float(ticker['ticker']['last'])
elif pair == '2' :
	pair = 'LTC_USD'
	selling = 'LTC'
	fore = 'USD'
	strpair = 'LTC/USD'
	ticker = ltc_usd_query()
	ticker = float(ticker['ticker']['last'])
elif pair == '3' :
	pair = 'LTC_BTC'
	selling = 'LTC'
	fore = 'BTC'
	strpair = 'LTC/BTC'
	ticker = ltc_btc_query()
	ticker = float(ticker['ticker']['last'])	
else :
	print("Error")

amount = input('What amount of coins would you like to sell if stop-loss is triggered?: ')
amount = float(amount)

stop = input('What rate would you like to set your stop-loss price at: ')		
stop = float(stop)
rate = stop

type = 'sell'




print('\n If', selling, 'reaches', fore, stop, 'or less, then', amount, selling, 'will be sold for', stop, fore,'each. \n')
yesno = input('Would you like to start? y/n:')

if yesno == 'y' :

	while 1==1 :
		if ticker <= stop :
			print('Placing order {}.'.format([pair, type, rate, amount]))	
			self.locknonce.acquire()
			response = api.trade(pair, type, rate, amount)
			self.locknonce.release()
			if response and 'success' in response.keys():
				if response['success'] == 1:
					print('Order placed successfully.')
					
				else:
					print('Error placing order: {}'.format(response['error']))
			time.sleep(5)
			break
		
		elif ticker > stop :
			print('The current', selling,'price is', ticker, fore)
			time.sleep(5)
				
				

	print('Stop-loss triggered')	
	time.sleep(100)
else :
	print('Closing in 10 seconds')
	time.sleep(10)
