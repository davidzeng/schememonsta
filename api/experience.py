from base_page import RoutedPage
import home

class Experience(RoutedPage):
    @classmethod
    def path(cls):
        return '/experience'

    @classmethod
    def options(cls):
        return [home.HomePage]

    @classmethod
    def description(cls):
        return 'My experience as a programmer.'

    @classmethod
    def page_text(cls):
        line1 = "I've worked at various places over the years. Keep going to learn more about my jobs."
        line2 = "Or just <a href='dz_resume.pdf' target='__blank'>download my resume</a>."
        return "<br/>".join([line1, line2])