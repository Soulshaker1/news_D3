from django import template


register = template.Library()


CURRENCIES_SYMBOLS = {
   'nigga': '*',
   'usd': '$',
}


@register.filter()
def currency(value, code='nigga'):
   """
   value: значение, к которому нужно применить фильтр
   code: код валюты
   """
   postfix = CURRENCIES_SYMBOLS[code]

   return f'{value} {postfix}'