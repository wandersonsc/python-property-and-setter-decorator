import pytest
from enhancing_class_attribute import Article
from slugify import slugify


@pytest.fixture(scope="module")
def article():
    article = Article(
        "Django is probably the best framework out there",
        "Django and React, best combo ever",
        "Django, Python, API, React",
        "Jack",
        "Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It's free and open source"
    )
    return article


def test_slugify_title(article):
    """ Test slugify method """

    slug = slugify(article.title.title())

    assert article.get_slug() == slug


def test_repr_method(article):
    """ Test repr method """

    assert (repr(article)) == F"Article({article.title.title()})"


def test_meta_description_method(article):
    """ Test meta description method """

    assert article.meta_description == article._meta_description
