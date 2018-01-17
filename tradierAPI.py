import requests
import urllib2
import json

baseurl = 'https://sandbox.tradier.com/v1/markets/quotes?symbols=SPY,TSLA,EEM'
accessToken = 'Your Token;




def main():
    req = urllib2.Request(baseurl)
    req.add_header('Authorization', 'Bearer {}'.format(accessToken))
    req.add_header('Accept', 'application/json')
    f = urllib2.urlopen(req)
    quotes = f
    quotes = json.load(quotes)
    quotes = quotes['quotes']['quote']
    tickerstring = ''
    for x in quotes:
        singleString = x['symbol'] + " " + str(x['last']) + " " + str(x['change_percentage'])
        tickerstring += " " + singleString
    print tickerstring




if __name__ == '__main__':
    main()
