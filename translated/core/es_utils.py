desde selenium.webdriver.remote.webdriver importar WebDriver

desde la configuración principal de importación
desde el núcleo importar TutorialBarScraper
desde la importación principal de UdemyActions


def redeem_courses(driver: WebDriver, ajustes: Ajustes,choice):
    """
    Método para extraer cursos de tutorialbar.com y matricularse en ellos en udemy

    :return:
    """
    tb_scraper = TutorialBarScraper()
    udemy_actions = UdemyActions(driver, settings)
    udemy_actions.login() # iniciar sesión una vez fuera mientras el bucle
    mientras verdadera:
        udemy_course_links = tb_scraper.run(elección)

        para curse_link en udemy_course_links:
            intentar:
                udemy_actions.redeem(course_link)
                if settings.is_ci_build:
                    volver
            excepto KeyboardInterrupt:
                subir
            excepto excepción:
                if settings.is_ci_build:
                    volver
                impresión(
                    "No se puede inscribir en este curso porque ya lo has reclamado o el navegador"
                    "ventana ha sido cerrada!")

        impresión(
            "Pasando a la siguiente página de la lista de cursos en tutorialbar.com")
