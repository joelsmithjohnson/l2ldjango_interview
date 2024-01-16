from django import template
import datetime

register = template.Library()

@register.filter
def l2l_dt(value):
    """Converts either an iso date string or a datetime object to the correct format"""
    output_format_string = "%Y-%m-%d %H:%M:%S"
    if type(value) is str:
        return datetime.datetime.fromisoformat(value).strftime(output_format_string)   
    if type(value) is datetime.datetime:
        return value.strftime(output_format_string)