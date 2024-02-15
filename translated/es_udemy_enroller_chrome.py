# Instalar todos los requisitos ejecutando requirements.py en IDLE o seguir las instrucciones alternativas en

desde selenium importar webdriver
desde webdriver_manager.chrome importar ChromeDriverManager

desde la configuración principal de importación
desde core.utils importar redeem_courses

settings = Settings()
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
chrome_options = Ninguna
if settings.is_ci_build:
    desde las opciones de importación de selenium.webdriver.chrome.options

    # Tener el agente de usuario con el parámetro Headless siempre llevaba a la comprobación de robot
    usuario_agente = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/85.0.4183.102 "
        "Safari/537.36")
    chrome_options = Opciones()
    # Necesitamos correr sin cabeza cuando usamos github CI
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-agent={0}".format(user_agent))
    chrome_options.add_argument("--window-size=1325x744")
    print("Esto es una ejecución IC")

driver = webdriver.Chrome(ChromeDriverManager().install(),
                          options=chrome_options)

# Maximiza la ventana del navegador ya que Udemy tiene un diseño receptivo y el código sólo funciona
driver.maximize_window()
# en el diseño maximizado

intentar:
    redeem_courses(driver, settings, choice)
    if settings.is_ci_build:
        print("Hemos intentado suscribirnos a 1 curso de udemy")
        print("Ending test")
excepto KeyboardInterrupt:
    print("Salir del script")
excepto excepción como:
    print("Error: {}".format(e))
finalmente:
    print("Cerrando navegador")
    driver.quit()
