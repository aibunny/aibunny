from  django import template
import readtime

register = template.Library()

def read(html):
    MReadTime= readtime.of_text(html) 
    HReadTime =readtime.of_html(html)
    total=  HReadTime +  MReadTime
    return total

register.filter('readtime',read)
    