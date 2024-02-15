# Instalar todos los requisitos ejecutando requirements.py en IDLE o seguir las instrucciones alternativas en
# https://github.com/aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE/ Asegúrese de que tiene
# ¡Se han borrado todos los detalles de pago guardados en tu cuenta de Udemy y el navegador! Para firefox necesita instalar manualmente el
# controlador en Arch Linux (sudo pacman -S geckodriver). No probado en otras plataformas.
desde selenium importar webdriver

desde la configuración principal de importación
desde core.utils importar redeem_courses

settings = Settings()

driver = webdriver.Firefox()

# Maximiza la ventana del navegador ya que Udemy tiene un diseño receptivo y el código sólo funciona
driver.maximize_window()

# en el diseño maximizado

intentar:
    redeem_courses(driver, settings)
excepto KeyboardInterrupt:
    print("Salir del script")
excepto excepción como:
    print("Error: {}".format(e))
finalmente:
    print("Cerrando navegador")
    driver.quit()
