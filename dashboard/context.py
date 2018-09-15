import json
import os


def dashboard_nav(request):
    """
    Provide menu data

    :param request: Django request (only for interface adherence, not needed)
    :return:  dictionary of menu entries
    """
    menu_file = os.path.join(os.path.dirname(__file__), 'menu.json')
    with open(menu_file, 'r') as _:
        context = {'dashboard_nav': json.load(_)}
    return context
