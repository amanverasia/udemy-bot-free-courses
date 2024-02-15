de importación multiprocessing.dummy Pool
desde la lista de importación

importar solicitudes
desde bs4 importar BeautifulSoup


class TutorialBarScraper:
	"""
	Contiene cualquier lógica relacionada con la eliminación de datos de tutorialbar.com
	"""

	DOMAIN = "https://www.tutorialbar.com"

	def __init__(self):
		self.current_page = 0
		self.last_page = Ninguna
		self.links_por_página = 12

	def run(self, choice) -> List:
		"""
		Ejecuta los pasos para raspar los enlaces de tutorialbar.com

		Lista :return: de enlaces de cupón de udemy
		"""
		
		print(tipo(elección))
		impresión(elección)
		página actual + = 1
		#print("Por favor espera: Obteniendo la lista de cursos de tutorialbar.com...")
		if(choice=='1'):
			
			course_links = self.get_course_links(elección,
				f"{self.DOMAIN}/category/it-software/page/{self.current_page}/"
			)
		elif(elección=='2'):
			course_links = self.get_course_links(elección,
				f"{self.DOMAIN}/categoría/desarrollo/página/{self.current_page}/"
			)
		elif(elección=='3'):
			course_links = self.get_course_links(elección,
				f"{self.DOMAIN}/category/finance-accounting/page/{self.current_page}/"
			)
		elif(choice=='4'):
			course_links = self.get_course_links(elección,
				f"{self.DOMAIN}/category/design/page/{self.current_page}/"
			)
		elif(elección=='5'):
			course_links = self.get_course_links(elección,
				f"{self.DOMAIN}/categoría/negocio/página/{self.current_page}/"
			)
		elif(elección=='6'):
			course_links = self.get_course_links(elección,
				f"{self.DOMAIN}/category/marketing/page/{self.current_page}/"
			)
		elif(choice=='7'):
			course_links = self.get_course_links(elección,
				f"{self.DOMAIN}/categoría/fitness/página/{self.current_page}/"
			)
		elif(elección=='8'):
			course_links = self.get_course_links(elección,
				f"{self.DOMAIN}/category/office-productivity/page/{self.current_page}/"
			)
		elif(elección=='9'):
			course_links = self.get_course_links(elección,
				f"{self.DOMAIN}/categoría/fotografia/página/{self.current_page}/"
			)
		elif(elección=='10'):
			course_links = self.get_course_links(elección,
				f"{self.DOMAIN}/category/personal-development/{self.current_page}/"
			)
		elif(choice=='11'):
			course_links = self.get_course_links(elección,
				f"{self.DOMAIN}/category/teaching-academics/page/{self.current_page}/"
			)




		no:
			course_links = self.get_course_links(elección,
				f"{self.DOMAIN}/todos-cursos/página/{self.current_page}/"
			)
		impresión(f"Página: {self.current_page} de {self.last_page} raspado\n")
		udemy_links = self.Today_udemy_course_links(course_links)

		# para el contador, curso en enumerate(udemy_links):
		# print(f"Link recibido {counter + 1} : {course}")
		#  print('\n\n')
		# print(f'Links in list format: {udemy_links}\n\n')
		devolver enlaces udemy_

	def is_first_loop(self) -> bool:
		"""
		Comprobación simple para ver si es la primera vez que ejecutamos

		:return: boolean showing if this is the first loop of the script
		"""
		devolver self.current_page == 1

	def get_course_links(self,choice, url: str) -> Lista:
		"""
		Obtiene la url de las páginas que contienen el enlace udemy que queremos obtener

		:param str url: La url de la que scrape los datos
		:return: list of pages on tutorialbar.com that contain Udemy coupons
		"""
		respuesta = requests.get(url=url)
		soup = BeautifulSoup(response.content, "html.parser")
		if(choice=='99'):
			links = soup.find("div", class_="rh-post-wrapper").find_all("a")
		no:
			links = soup.find("div", class_="main-side clearfix").find_all("a")
		self.last_page = enlaces[-2].text
		cursos = []

		x = 0
		for _ in range(self.links_per_page):
			courses.append(enlaces[x].get("href"))
			x += 3

		regresar cursos

	@staticmethod
	def get_udemy_course_link(url: str) -> str:
		"""
		Obtiene el enlace de curso de udemy

		:param str url: La url de la que scrape los datos
		:return: enlace de cupón del curso de udemy
		"""
		respuesta = requests.get(url=url)
		soup = BeautifulSoup(response.content, "html.parser")
		udemy_link = soup.find("span", class_="rh_button_wrapper").find("a").get("href")
		devolver udemy_link

	def collect_udemy_course_links(self, courses: List[str]) -> Lista:
		"""
		Búsqueda en hilo de los enlaces del curso udemy desde tutorialbar.com

		:param list courses: Una lista de enlaces de curso de tutorialbar.com que queremos obtener los enlaces de udemy para
		Lista :return: de enlaces de udemy
		"""
		thread_pool = Pool()
		resultados = thread_pool.map(self.get_udemy_course_link, cursos)
		thread_pool.close()
		thread_pool.join()
		devolver resultados
