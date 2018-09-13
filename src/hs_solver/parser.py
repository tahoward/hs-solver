import re

from bs4 import BeautifulSoup
from bs4.element import Comment


HREF_PATTERN = re.compile(r"^/(?!/)")


def get_start_link(document=None):
    soup = BeautifulSoup(document, features="html.parser")
    link = soup.body.find("a", attrs={"class": "btn"}).get("href")

    return link


def get_message(document=None):
    soup = BeautifulSoup(document, features="html.parser")

    try:
        elements = soup.body.findAll(text=True)
        visible_elements = filter(visible, elements)
        message = get_string(elements=visible_elements)

    except AttributeError:
        message = soup.string

    return "Message: {}".format(message)


def visible(element=None):
    excluded_tags = ["a", "span"]

    if element.parent.name in excluded_tags:
        return False

    if isinstance(element, Comment):
        return False

    return True


def get_comments(document=None):
    soup = BeautifulSoup(document, features="html.parser")
    elements = soup.body.findAll(text=True)
    comment_elements = filter(comment, elements)

    return get_string(elements=comment_elements)


def comment(element=None):
    if isinstance(element, Comment):
        return True

    return False


def get_string(elements=None):
    element_list = []

    for element in elements:
        if not element.isspace():
            element_list.append(element.strip())

    return " ".join(element_list)


def get_css_link(document=None):
    soup = BeautifulSoup(document, features="html.parser")
    style_sheets = soup.head.findAll("link", attrs={"rel": "stylesheet"})

    for style_sheet in style_sheets:
        href = style_sheet.get("href")
        if HREF_PATTERN.match(href):
            return href
