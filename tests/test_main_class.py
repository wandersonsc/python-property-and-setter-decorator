from enhancing_class_attribute import Article
from slugify import slugify


def test_slugify_title():
    """ Test slugify method """

    article = Article(
        "Django is probably the best framework out there",
        "Artitle aout Python and Django"
    )
    slug = slugify(article.title)

    assert article.get_slug() == slug
