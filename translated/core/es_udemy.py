importar tiempo

desde selenium.common.exceptions importar NoSuchElementException
desde selenium.webdriver.common.by importar Por
de selenium.webdriver.support importar expected_conditions como CE
desde selenium.webdriver.support.ui importar WebDriverWait


clases UdemyActions:
    """
    Contiene cualquier lógica relacionada con la interacción con el sitio web de udemy
    """

    DOMAIN = "https://www.udemy.com"

    def __init__(autor, driver, ajustes):
        self.driver = driver
        self.settings = ajustes
        self.logged_in = False

    def login(self) -> Ninguno:
        """
        Inicia sesión en tu cuenta de udemy

        :return: None
        """
        si no self.logged_in:
            self.driver.get(f"{self.DOMAIN}/join/login-popup/")

            email_element = self.driver.find_element_by_name("email")
            email_element.send_keys(self.settings.email)

            password_element = self.driver.find_element_by_name("contraseña")
            contraseña_element.send_keys(self.settings.password)

            self.driver.find_element_by_name("Enviado").click()
            self.logged_in = Verdadero

    def redem(self, url: str) -> Ninguno:
        """
        Canjea la url del curso pasada en

        :param str url: URL del curso a canjear
        :return: None
        """
        self.driver.get(url)
        print("Intentando inscribirse: " + self.driver.title)

        # Si el usuario ha configurado los idiomas, compruebe que es una opción soportada
        if self.settings.languages:
            locale_xpath = "//div[@data-purpose='lead-course-locale']"
            element_text = (WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((por.XPATH, locale_xpath))).text)

            si element_text no está en self.settings.languages:
                print("Idioma del curso no deseado: {}".format(element_text))
                volver

        # Inscribirse ahora 1
        buy_course_button_xpath = "//button[@data-purpose='buy-this-course-button']"
        element_present = EC.presence_of_element_located(
            (Por.XPATH, buy_course_button_xpath))
        WebDriverWait(self.driver, 10).until(element_present).click()

        enroll_button_xpath = "//*[@class='udemy pageloaded']/div[1]/div[2]/div/div/div/div[2]/form/div[2]/div/div[4]/button"
        # Inscribirse ahora 2
        element_present = EC.presence_of_element_located((
            Por.XPATH,
            enroll_button_xpath,
        ))
        WebDriverWait(self.driver, 10).until(element_present)

        # Comprueba si el código postal existe antes de hacer esto
        si self.settings.zip_code:
            # Supongamos que a veces zip no es necesario porque el script fue originalmente empujado sin esto
            intentar:
                zipcode_element = self.driver.find_element_by_id(
                    "dirección de billingSegundoEntrada")
                código zipcode_element.send_keys(self.settings.zip_code)

                # Después de poner el código postal, la página se actualiza y desactiva el botón de inscripción para una división
                # segundo.
                time.sleep(1)
            excepto NochElementException:
                pasar

        udemy_enroll_element_2 = self.driver.find_element_por_xpath(
            enroll_button_xpath) # Udemy
        udemy_enroll_element_2.click()
