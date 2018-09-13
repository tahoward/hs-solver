"""
hs-solver

Usage:
  hs-solver --name=<name> --email=<email>
            [--phone=<phone>]
            [--twitter=<twitter>]
            [--hirable]

  hs-solver -h | --help
  hs-solver --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.
  -n <name> --name=<name>           Your name.
  -e <email> --email=<email>        Your email address.
  -p <phone> --phone=<phone>        Your phone number.
  -t <twitter> --twitter=<twitter>  Your twitter account URL.
  -h --hirable                      Enable hirable mode.

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/tahoward/hs-solver
"""  # noqa

import hs_solver.parser as parser

from docopt import docopt

from hs_solver import __version__ as VERSION

from hs_solver.common import HS_URL
from hs_solver.connection import Connection

from hs_solver.puzzles import math
from hs_solver.puzzles import haystack
from hs_solver.puzzles import breadcrumb
from hs_solver.puzzles import trueblue
from hs_solver.puzzles import endgame


def main():
    options = docopt(__doc__, version=VERSION)
    connection = Connection()
    response = connection.call(endpoint=HS_URL)
    link = parser.get_start_link(document=response.text)
    response = connection.call(endpoint=HS_URL + link)

    # Do math!
    response = math.solve(connection=connection, response=response)

    # Find the needle!
    response = haystack.solve(connection=connection, response=response)

    # Follow the breadcrumbs!
    response = breadcrumb.solve(connection=connection, response=response)

    # Solve the riddle!
    response = trueblue.solve(connection=connection, response=response)

    # End game!
    endgame.solve(connection=connection, response=response, options=options)
