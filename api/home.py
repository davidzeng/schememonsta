from base_page import RoutedPage
import me, contact

class HomePage(RoutedPage):
    @classmethod
    def path(cls):
        return '/home'

    @classmethod
    def options(cls):
        return [me.AboutMe, contact.Contact]

    @classmethod
    def description(cls):
        return 'This is the home page.'
