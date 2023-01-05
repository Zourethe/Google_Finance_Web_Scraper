# Imports.
import requests

def price(code):
    request = requests.get('https://www.google.com/finance/quote/{}'.format(code)).text
    posStart = request.find('YMlKec fxKbKc')
    posEnd = posStart + 13
    
    print(request[posStart:posEnd])


codeA = input(str('Type the code that comes after "https://www.google.com/finance/quote/": '))
price(codeA)

