from base_page import RoutedPage
import me

class HomePage(RoutedPage):
    @classmethod
    def path(cls):
        return '/home'

    @classmethod
    def options(cls):
        return [me.AboutMe, me.Contact]

    @classmethod
    def description(cls):
        return 'This is the home page.'
