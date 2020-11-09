from selenium.webdriver.remote.webdriver import WebDriver

from core import TutorialBarScraper
links = []
tb_scraper = TutorialBarScraper()

print('1. IT software')
print('2. Development')
print('3. Finance Accounting')
print('4. Design')
print('5. Business')
print('6. Marketing')
print('7. Health and Fitness')
print('8. Office Productivity')
print('9. Photography')
print('10. Personal Development')
print('11. Teaching and Academics')
print('99. All Courses')
choice = input('Please select what category you want? :')
while True:
    udemy_course_links = tb_scraper.run(choice)
    links = links + udemy_course_links
print(links)
print(len(links))
