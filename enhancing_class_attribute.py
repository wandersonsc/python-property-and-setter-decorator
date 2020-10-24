import textwrap
from slugify import slugify


class Article:

    def __init__(self, title, description, keywords, author, meta_description):

        self.title = title.title()
        self.description = description
        self.keywords = keywords
        self.author = author
        self.meta_description = meta_description

    # Getter
    @property
    def meta_description(self):

        return self._meta_description

    # Setter
    @meta_description.setter
    def meta_description(self, value):

        self._meta_description = textwrap.shorten(
            value, width=160)

    def __repr__(self):

        return F"{self.__class__.__name__}({self.title})"

    def get_slug(self):

        slug = slugify(self.title)
        return slug
