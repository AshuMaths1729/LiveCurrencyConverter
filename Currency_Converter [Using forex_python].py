# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 23:45:47 2018

#Currency Converter

@author: Ashutosh Agrahari
"""
def curr_convrt():

    print("What you want to deal with: \nA) Physical Currencies\nB) Bicoins\n")
    choice = input()
    
    if(choice == "A"):
        print("Enter currency to be converted from: ", sep = "",end ="")
        c1 = input()
        print("Enter Amount: ",sep="", end = "")
        amt = int(input())
        print("Enter currency to be converted to: ",sep="", end = "")
        c2 = input()
        c2_amt = forex(c1,c2,amt)
        print(amt, c1, "in",c2,"is","{0:.2f}".format(c2_amt),c2,sep=" ")
    
    elif(choice == "B"):
        print("Enter currency for which to see rates: ")
        c = input()
        c_amt = bitcoin(c)
        print("1 Bitcoin = ",c_amt," ",c)
    else:
        print("Wrong input")
        

def forex(c1,c2,amt):
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()
    return c.convert(c1, c2, amt)

def bitcoin(cMT):
    from forex_python.bitcoin import BtcConverter
    c = BtcConverter()
    return c.get_latest_price(cMT) 