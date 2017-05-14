#!/usr/bin/python
import urllib
import time

stocks_to_pull = ['AMD', 'BAC', 'MSFT', 'TXN', 'GOOG']

def pull_data_for_stock(stock):
    stock_file = stock + '.txt'
    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
    print ("Data from URL: " + url)
    f = urllib.urlopen(url)
    source = f.read().decode('utf-8')
    
    split_source = source.split('\n')
    for line in split_source:
          saveFile = open(stock_file,'a')
          linetoWrite = line + '\n'
          saveFile.write(linetoWrite)

    print('Pulled', stock)
    print('...')
    time.sleep(.5)

if __name__=="__main__":
    for stock in stocks_to_pull: 
        print ("working on " + stock)    
        pull_data_for_stock(stock)

