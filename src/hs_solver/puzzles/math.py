import hs_solver.parser as parser

from hs_solver.common import HS_URL


def solve(connection=None, response=None):
    # This doesn't appear to be dynamic at all.

    # Start!
    print(parser.get_message(document=response.text))

    # Just send 54.
    response = connection.call(endpoint=HS_URL + "/54")
    print(parser.get_message(document=response.text))

    # Then send the base13 value of 54, 42
    return connection.call(endpoint=HS_URL + "/42")
