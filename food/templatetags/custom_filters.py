from django import template

register = template.Library()

@register.filter
def currency(value):
  return f"₹{value}"

@register.filter
def discount(value, percent):
  price = float(value)
  discount = float(percent)
  return f"{price * (1 - discount / 100):.2f}"
