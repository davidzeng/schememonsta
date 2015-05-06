from base_page import RoutedPage
import me, contact, credits, experience

class HomePage(RoutedPage):
    @classmethod
    def path(cls):
        return '/home'

    @classmethod
    def options(cls):
        return [me.AboutMe, contact.Contact, credits.Credits, experience.Experience]

    @classmethod
    def description(cls):
        return 'Go back to home base.'

    @classmethod
    def page_text(cls):
        return "You're at base camp. Go explore the other parts of my site!"
