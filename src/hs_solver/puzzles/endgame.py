import hs_solver.parser as parser


def solve(connection=None, response=None, options=None):
    print(parser.get_message(document=response.text))
    response = connection.call(endpoint=response.request.url, post=True)
    print(parser.get_message(document=response.text))

    params = {
        "name": options["--name"],
        "email": options["--email"]
    }

    if options["--phone"]:
        params["phone"] = options["--phone"]

    if options["--twitter"]:
        params["twitter"] = options["--twitter"]

    if options["--hirable"]:
        params["hirable"] = "true"

    response = connection.call(
        endpoint=response.request.url,
        params=params,
        post=True
    )

    print(parser.get_message(document=response.text))
