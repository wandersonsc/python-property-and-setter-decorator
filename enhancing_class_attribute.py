from slugify import slugify


class Article:

    def __init__(self, title, description):

        self.title = title
        self.description = description

    def __repr__(self):

        return F"{self.__class__.__name__}({self.title})"

    def get_slug(self):

        slug = slugify(self.title)
        return slug
