import re

import hs_solver.parser as parser

from hs_solver.common import HS_URL


COOKIE_PATTERN = re.compile(r"info=([\"])?([^\";]+)")
MESSAGE_PATTERN = re.compile(r"(Add|Subtract)? (?!12345|54321)([0-9]+|monster)") # noqa


def solve(connection=None, response=None, char_list=None, previous_crumb=None):
    if not char_list:
        char_list = []

    # Follow the breadcrumbs! Clues are in the response header.
    message = parser.get_message(document=response.text)
    print(message)

    cookie = response.headers['Set-Cookie']
    info = COOKIE_PATTERN.match(cookie).group(2)

    if info != "follow the breadcrumbs":
        search_result = MESSAGE_PATTERN.search(message)
        operator = search_result.group(1)
        breadcrumb = search_result.group(2)

        if operator:
            if operator == "Add":
                breadcrumb = int(previous_crumb) + int(breadcrumb)

            if operator == "Subtract":
                breadcrumb = int(previous_crumb) - int(breadcrumb)

        char_list.append(info.encode())
        response = connection.call(HS_URL + "/breadcrumbs/" + str(breadcrumb))
        return solve(
            connection=connection,
            response=response,
            char_list=char_list,
            previous_crumb=breadcrumb
        )
    else:
        riddle = b"".join(char_list).decode('unicode_escape')
        print("Riddle:\n" + riddle)

        return response
