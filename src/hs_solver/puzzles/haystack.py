import re

import hs_solver.parser as parser

from hs_solver.common import HS_URL


def solve(connection=None, response=None):
    print(parser.get_message(document=response.text))

    # Get haystack from the response body.
    haystack = parser.get_comments(document=response.text)

    # Regex for finding the needle.
    needle = re.search(r"([a-z]{4}[A-Z]{4})", haystack).group(1)

    response = connection.call(endpoint=HS_URL + "/" + needle)

    return response
