from django import template
import timeago
import datetime

register = template.Library()


@register.simple_tag
def calculate_time_age(date):
    now = datetime.datetime.now(datetime.timezone.utc) + \
        datetime.timedelta(seconds=60 * 3.4)
    return timeago.format(date, now)
