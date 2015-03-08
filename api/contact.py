from base_page import RoutedPage
import home

class Contact(RoutedPage):
    @classmethod
    def path(cls):
        return '/contact'

    @classmethod
    def options(cls):
        return [home.HomePage]

    @classmethod
    def description(cls):
        return 'How to contact me.'

    @classmethod
    def page_text(cls):
        return "Here's a list of the ways you can contact me:"

    @classmethod
    def page_json(cls):
        return dict(email='david.tao.zeng@gmail.com',
                    linkedin="<a href='http://www.linkedin.com/pub/david-zeng/9/a22/14a' target='_blank'>Linkedin</a>",
                    github="<a href='http://github.com/davidzeng' target='_blank'>Github</a>")