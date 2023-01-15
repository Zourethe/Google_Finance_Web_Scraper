# Imports.
from requests import get
from re import match

# Price function.
def price(quote):
    request = get('https://www.google.com/finance/quote/{}'.format(quote)).text
    start = request.find('YMlKec fxKbKc')
    end = start + 15
    limit = end + 100
    text = request[end:limit]
    counter = match('.+([0-9])[^0-9]*$', text)
    numEnd = counter.start(1) + 1
    return float(text[:numEnd].replace(',', ''))