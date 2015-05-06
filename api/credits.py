from base_page import RoutedPage
import home

class Credits(RoutedPage):
    @classmethod
    def path(cls):
        return '/credits'

    @classmethod
    def options(cls):
        return [home.HomePage]

    @classmethod
    def description(cls):
        return 'People that helped to make this!'

    @classmethod
    def page_text(cls):
        line1 = "I certainly didn't build the javascript portion of this myself. I used a plugin called <a href='http://terminal.jcubic.pl/' target='_blank'>JQueryTerminal</a>."
        line2 = "I also received color and other small design help from <a href='http://www.jessicachoy.com/' target='_blank'>Jessica Choy</a>."
        return '<br/>'.join([line1, line2])
