import json
import os


def menu(request):
    """
    Provide menu data

    :param request: Django request (only for interface adherence, not needed)
    :return:  dictionary of menu entries
    """
    menu_file = os.path.join(os.path.dirname(__file__), 'menu.json')
    with open(menu_file, 'r') as _:
        context = {'menu': json.load(_)}
    return context
