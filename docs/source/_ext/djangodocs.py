# -*- coding: utf-8 -*-
"""
    djangodocs
    ~~~~~~~~~~

    :copyright: Copyright 2016 by The Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


def setup(app):
    """
    Dummy extension to enable cross-links to the official Django documentation
    when referring to Django-specific items such as:

    * Settings
    * Template Tags
    * Template Filters
    * Model Field Lookups

    :param app:  Sphinx application object
    :return:     void
    """
    app.add_crossref_type(
        directivename="setting",
        rolename="setting",
        indextemplate="pair: %s; setting",
    )
    app.add_crossref_type(
        directivename="templatetag",
        rolename="ttag",
        indextemplate="pair: %s; template tag"
    )
    app.add_crossref_type(
        directivename="templatefilter",
        rolename="tfilter",
        indextemplate="pair: %s; template filter"
    )
    app.add_crossref_type(
        directivename="fieldlookup",
        rolename="lookup",
        indextemplate="pair: %s; field lookup type",
    )
