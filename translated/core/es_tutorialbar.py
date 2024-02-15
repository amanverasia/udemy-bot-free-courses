from multiprocessing.dummy import Pool
from typing import List

import requests
from bs4 import BeautifulSoup


class TutorialBarScraper:
	"""
	Contains any logic related to scraping of data from tutorialbar.com
	"""

	DOMAIN = "https://www.tutorialbar.com"

	def __init__(self):
		self.current_page = 0
		self.last_page = None
		self.links_per_page = 12

	def run(self, choice) -> List:
		"""
		Runs the steps to scrape links from tutorialbar.com

		:return: list of udemy coupon links
		"""
		
		print(type(choice))
		print(choice)
		self.current_page += 1
		#print("Please Wait: Getting the course list from tutorialbar.com...")
		if(choice=='1'):
			
			course_links = self.get_course_links(choice,
				f"{self.DOMAIN}/category/it-software/page/{self.current_page}/"
			)
		elif(choice=='2'):
			course_links = self.get_course_links(choice,
				f"{self.DOMAIN}/category/development/page/{self.current_page}/"
			)
		elif(choice=='3'):
			course_links = self.get_course_links(choice,
				f"{self.DOMAIN}/category/finance-accounting/page/{self.current_page}/"
			)
		elif(choice=='4'):
			course_links = self.get_course_links(choice,
				f"{self.DOMAIN}/category/design/page/{self.current_page}/"
			)
		elif(choice=='5'):
			course_links = self.get_course_links(choice,
				f"{self.DOMAIN}/category/business/page/{self.current_page}/"
			)
		elif(choice=='6'):
			course_links = self.get_course_links(choice,
				f"{self.DOMAIN}/category/marketing/page/{self.current_page}/"
			)
		elif(choice=='7'):
			course_links = self.get_course_links(choice,
				f"{self.DOMAIN}/category/health-fitness/page/{self.current_page}/"
			)
		elif(choice=='8'):
			course_links = self.get_course_links(choice,
				f"{self.DOMAIN}/category/office-productivity/page/{self.current_page}/"
			)
		elif(choice=='9'):
			course_links = self.get_course_links(choice,
				f"{self.DOMAIN}/category/photography/page/{self.current_page}/"
			)
		elif(choice=='10'):
			course_links = self.get_course_links(choice,
				f"{self.DOMAIN}/category/personal-development/page/{self.current_page}/"
			)
		elif(choice=='11'):
			course_links = self.get_course_links(choice,
				f"{self.DOMAIN}/category/teaching-academics/page/{self.current_page}/"
			)




		else:
			course_links = self.get_course_links(choice,
				f"{self.DOMAIN}/all-courses/page/{self.current_page}/"
			)
		print(f"Page: {self.current_page} of {self.last_page} scraped\n")
		udemy_links = self.gather_udemy_course_links(course_links)

		# for counter, course in enumerate(udemy_links):
		# 	print(f"Received Link {counter + 1} : {course}")
		#  print('\n\n')
		#  print(f'Links in list format: {udemy_links}\n\n')
		return udemy_links

	def is_first_loop(self) -> bool:
		"""
		Simple check to see if this is the first time we have executed

		:return: boolean showing if this is the first loop of the script
		"""
		return self.current_page == 1

	def get_course_links(self,choice, url: str) -> List:
		"""
		Gets the url of pages which contain the udemy link we want to get

		:param str url: The url to scrape data from
		:return: list of pages on tutorialbar.com that contain Udemy coupons
		"""
		response = requests.get(url=url)
		soup = BeautifulSoup(response.content, "html.parser")
		if(choice=='99'):
			links = soup.find("div", class_="rh-post-wrapper").find_all("a")
		else:
			links = soup.find("div", class_="main-side clearfix").find_all("a")
		self.last_page = links[-2].text
		courses = []

		x = 0
		for _ in range(self.links_per_page):
			courses.append(links[x].get("href"))
			x += 3

		return courses

	@staticmethod
	def get_udemy_course_link(url: str) -> str:
		"""
		Gets the udemy course link

		:param str url: The url to scrape data from
		:return: Coupon link of the udemy course
		"""
		response = requests.get(url=url)
		soup = BeautifulSoup(response.content, "html.parser")
		udemy_link = soup.find("span", class_="rh_button_wrapper").find("a").get("href")
		return udemy_link

	def gather_udemy_course_links(self, courses: List[str]) -> List:
		"""
		Threaded fetching of the udemy course links from tutorialbar.com

		:param list courses: A list of tutorialbar.com course links we want to fetch the udemy links for
		:return: list of udemy links
		"""
		thread_pool = Pool()
		results = thread_pool.map(self.get_udemy_course_link, courses)
		thread_pool.close()
		thread_pool.join()
		return results
