from base_page import RoutedPage
import home

class AboutMe(RoutedPage):
    @classmethod
    def path(cls):
        return '/about_me'

    @classmethod
    def options(cls):
        return [home.HomePage, WhyIMadeThisWebsite, MyHobbies]

    @classmethod
    def description(cls):
        return 'Learn more about me and my website.'

    @classmethod
    def page_text(cls):
        line1 = "My name is David Zeng and I am a software engineer currently working at Clinkle."
        br = ""
        line2 = "I specialize in working on the backend, designing API's and working on general architecture."
        line3 = "At work, I enjoy building tools and platforms that people can interact with."
        line4 = "Data driven decision making in real world applications also appeals to my (former) analyst nature."
        return '<br/>'.join([line1, br, line2, line3, line4])

class WhyIMadeThisWebsite(RoutedPage):
    @classmethod
    def path(cls):
        return '/why'

    @classmethod
    def options(cls):
        return [home.HomePage, AboutMe, MyHobbies]

    @classmethod
    def description(cls):
        return 'Why did you build your site like this?'

    @classmethod
    def page_text(cls):
        line1 = "As someone who mostly focuses on the backend, I wanted a website that reflected my interests in engineering."
        line2 = "I've always wanted to build a website but didn't want to focus on designing layout."
        br = ""
        line3 = "One day it came to mind that a terminal interface with a simple API backend is both minimalistic"
        line4 = "and demonstrates my preference in design. While designing this, I got to play around with Flask and Heroku."
        return '<br/>'.join([line1, line2, br, line3, line4])

class MyHobbies(RoutedPage):
    @classmethod
    def path(cls):
        return '/hobbies'

    @classmethod
    def options(cls):
        return [home.HomePage, WhyIMadeThisWebsite, AboutMe]

    @classmethod
    def description(cls):
        return 'My current hobbies, both athletic and lethargic in nature.'

    @classmethod
    def page_text(cls):
        return "When I'm not playing sports, I prefer to be in as inactive as possible."

    @classmethod
    def page_json(cls):
        return dict(Running="Running for 2 years. Hope to do the Toyko marathon in 2016 if I'm not injured.",
            Badminton="Playing for 8 years total in men's doubles (C Level) and mixed (Looking for Partner!).",
            Games="Hearthstone, Final Fantasy, The Last of Us, Catherine and To The Moon are recent favorites.")
