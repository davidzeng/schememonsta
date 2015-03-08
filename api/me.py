from base_page import RoutedPage
import home

class AboutMe(RoutedPage):
    @classmethod
    def path(cls):
        return '/about_me'

    @classmethod
    def options(cls):
        return [home.HomePage, Why]

    @classmethod
    def description(cls):
        return 'Learn more about me and my website.'

    @classmethod
    def page_text(cls):
        line1 = "My name is David Zeng and I am a software engineer currently working at Clinkle."
        line2 = "I specialize in working on the backend, designing API's and working on general architecture."
        return '<br/>'.join([line1, line2])

class Why(RoutedPage):
    @classmethod
    def path(cls):
        return '/why'

    @classmethod
    def options(cls):
        return [home.HomePage, AboutMe]

    @classmethod
    def description(cls):
        return 'Why did you build your site like this?'

    @classmethod
    def page_text(cls):
        line1 = "As someone who mostly focuses on the backend, I wanted a website that reflected my interests in engineering."
        line2 = "I've always wanted to build a website but didn't want to focus on designing layout."
        line3 = "One day it came to mind that a terminal interface with a simple API backend is both minimalistic"
        line4 = "and demonstrates my preference in design. While designing this, I got to play around with Flask, Heroku and"
        line5 = "just learned more in general."
        return '<br/>'.join([line1, line2, line3, line4, line5])
