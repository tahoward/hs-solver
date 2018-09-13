import cssutils

import hs_solver.parser as parser

from hs_solver.common import HS_URL


def solve(connection=None, response=None):
    css_link = parser.get_css_link(document=response.text)
    response = connection.call(endpoint=HS_URL + css_link)
    sheet = cssutils.parseString(response.text)
    true_blue = None

    for rule in sheet.cssRules:
        if rule.selectorText == ".true-blue":
            true_blue = rule.style.color[1:]

    response = connection.call(endpoint=HS_URL + "/" + true_blue)

    return response
