import re

class RoutedPage:
    @classmethod
    def path(cls):
        return NotImplementedError

    @classmethod
    def simple_path(cls):
        return cls.path()[1:] # remove the beginning slash

    @classmethod
    def options_dict(cls):
        page_list = cls.options()
        return dict(paths=dict([(x.simple_path(), dict(path=x.path(), text=x.description())) for x in page_list]),
                    page_text=cls.page_text(), page_json=cls.page_json(), page_heading=cls.page_heading())

    @classmethod
    def options(cls):
        return []

    @classmethod
    def description(cls):
        # what's shown to the users in the options page.
        return 'Go back to the top.'

    @classmethod
    def page_heading(cls):
        return re.sub('(?<=\w)([A-Z])', r' \1', cls.__name__)

    @classmethod
    def page_text(cls):
        # what's displayed as text on the page.
        return ''

    @classmethod
    def page_json(cls):
        # dictionary that'll get pretty printed into JSON
        return dict()