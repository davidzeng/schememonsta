from base_page import RoutedPage
import home

class AboutMe(RoutedPage):
    @classmethod
    def path(cls):
        return '/about_me'

    @classmethod
    def options(cls):
        return [home.HomePage]

    @classmethod
    def description(cls):
        return 'This page is about me.'

    @classmethod
    def page_text(cls):
        line1 = "My name is David Zeng and I am a software engineer currently working at Clinkle."
        line2 = "I specialize in working on the backend, designing API's and working on general architecture."
        return '<br/>'.join([line1, line2])


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
                    linkedin='https://www.linkedin.com/pub/david-zeng/9/a22/14a',
                    github='https://github.com/davidzeng')