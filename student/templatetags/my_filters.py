from django import template
register = template.Library()
@register.filter()
def isnumeric(self):
    item = self.item
    if item.isnumeric() is True:
        return True
    else:
        return False
