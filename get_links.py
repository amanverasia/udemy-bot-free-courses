from selenium.webdriver.remote.webdriver import WebDriver

from core import TutorialBarScraper
tb_scraper = TutorialBarScraper()
while True:
    udemy_course_links = tb_scraper.run()
