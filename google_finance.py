# Imports.
from requests import get as gt


# "price" function.
def price(quote):
    """Returns the price of the quote give in "quote: " """

    try:
        request_price = gt('https://www.google.com/finance/quote/{}'.format(quote)).text
        start_price = request_price.find('"YMlKec fxKbKc"')
        end_price = start_price + 16
        text_price = request_price[end_price:end_price + 200]
        nextdiv_price = text_price.find('</div>')
        content_price = text_price[:nextdiv_price]

        return content_price
    except:
        return ('Value not found.')


# "heading" function.
def heading(quote):
    """Returns the heading of the quote give in "quote: " """

    try:
        request_heading = gt('https://www.google.com/finance/quote/{}'.format(quote)).text
        start_heading = request_heading.find('"zzDege"')
        end_heading = start_heading + 9
        text_heading = request_heading[end_heading:end_heading + 200]
        nextdiv_heading = text_heading.find('</div>')
        content_heading = text_heading[:nextdiv_heading]

        return content_heading
    except:
        return ('Value not found.')


# "date" function.
def date(quote):
    """Returns the date of the quote give in "quote: " """

    try:
        request_date = gt('https://www.google.com/finance/quote/{}'.format(quote)).text
        start_date = request_date.find('"Vebqub"')
        end_date = start_date + 9
        text_date = request_date[end_date:end_date + 200]
        nextdiv_date = text_date.find('<a')
        content_date = text_date[:nextdiv_date]

        return content_date.replace('&middot;', '*')
    except:
        return ('Value not found.')


# "previous_close" function.
def previous_close(quote):
    """Returns the previous close price of the quote give in "quote: " """

    try:
        request_previous_close = gt('https://www.google.com/finance/quote/{}'.format(quote)).text
        start_previous_close = request_previous_close.find('"P6K39c"')
        end_previous_close = start_previous_close + 9
        text_previous_close = request_previous_close[end_previous_close:end_previous_close + 200]
        nextdiv_previous_close = text_previous_close.find('</div>')
        content_previous_close = text_previous_close[:nextdiv_previous_close]

        return content_previous_close
    except:
        return ('Value not found.')
