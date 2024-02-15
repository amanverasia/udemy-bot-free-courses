desde selenium.webdriver.remote.webdriver importar WebDriver

desde el núcleo importar TutorialBarScraper
enlaces = []
tb_scraper = TutorialBarScraper()

print('1. Software IT')
print('2. Desarrollo')
print('3. Contabilidad financiera')
print('4. Diseño)
print('5. Negocios)
print('6. Marketing')
print('7. Salud y Fitness ')
print('8. Productividad de oficina')
print('9. Fotografía')
print('10. Desarrollo personal')
print('11. Enseñanza y académicos')
print('99. Todos los cursos')
choice = input('Por favor seleccione qué categoría quiere? :')
mientras verdadera:
    udemy_course_links = tb_scraper.run(elección)
    enlaces = enlaces + enlaces udemy_course_links
impresión(enlaces)
print(len(links))
