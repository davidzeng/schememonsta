from base_page import RoutedPage
import home

class Experience(RoutedPage):
    @classmethod
    def path(cls):
        return '/experience'

    @classmethod
    def options(cls):
        return [home.HomePage, PocketGems, Clinkle]

    @classmethod
    def description(cls):
        return 'My experience as a programmer.'

    @classmethod
    def page_text(cls):
        line1 = "I've worked at various places over the years. Keep going to learn more about my jobs."
        line2 = "Or just <a href='dz_resume.pdf' target='__blank'>download my resume</a>."
        return "<br/>".join([line1, line2])


class PocketGems(RoutedPage):
    @classmethod
    def path(cls):
        return '/pocket_gems'

    @classmethod
    def options(cls):
        return [Experience, home.HomePage, Clinkle]

    @classmethod
    def description(cls):
        return 'The best mobile gaming company! - September 2011 - September 2014.'

    @classmethod
    def page_text(cls):
        return "I worked at Pocket Gems for 3 years, exploring a variety of roles from analytics/tools, \
        server and even spent time working on a game time building a specialized backend. \
        I eventually took on the position of server lead."

    @classmethod
    def page_json(cls):
        analytics = ["Integrated rollup system to aggregate granular player data for key player metrics.", 
        "Implemented tool to send push notifications in bulk via recipient querying in SQL.",
        "Ported and created data visualizations from PostgreSQL to Vertica database."]
        server = ["Architected custom backend specializing in server side validation and security.",
        "Transitioned unique player identification scheme across all games when iOS identifiers were deprecated.",
        "Build UA management tool with customizable per-advertiser callbacks to verify installation channel.",
        "Developed cross game achievement system with configurable goals and rewards.",
        "Prototyped and researched technologies for real time communication between users."]
        lead = ["Lead team of 4 engineers - held weekly 1-1's along with bi-weekly scrum and annual performance reviews.",
        "Manage weekly team goals with JIRA. Roadmap for large game-specific projects.",
        "Spoke as representative to Google about challenges on Cloud Platform."]
        return dict(Analytics=analytics,
                    Server=server,
                    Lead=lead)

class Clinkle(RoutedPage):
    @classmethod
    def path(cls):
        return '/clinkle'

    @classmethod
    def options(cls):
        return [Experience, home.HomePage, PocketGems]

    @classmethod
    def description(cls):
        return 'Mobile payments - September 2014 - Present.'

    @classmethod
    def page_text(cls):
        return "I worked in a team of 4 to support the payments platform and improve user engagement with the product"

    @classmethod
    def page_json(cls):
        return ["Worked on event queueing layer to allow for asynchronous task scheduling and completion.",
        "Built user referral and redemption program to promote and track user acquisition.",
        "Developed automated email and push onboarding system for early user engagement and retention."]
