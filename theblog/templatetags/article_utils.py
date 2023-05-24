from  django import template
import readtime

register = template.Library()

def read(html):
    HReadTime =readtime.of_html(html)
    total=  HReadTime
    return total

register.filter('readtime',read)
    