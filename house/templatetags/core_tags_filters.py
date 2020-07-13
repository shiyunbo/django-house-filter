from django import template

register = template.Library()


# used in django-filter preserve request paramters
@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    用于URL拼接参数并去重
    https://stackoverflow.com/questions/22734695/next-and-before-links-for-a-django-paginated-query/22735278#22735278
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()


