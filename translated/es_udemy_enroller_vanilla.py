# Instalar todos los requisitos ejecutando requirements.py en IDLE o seguir las instrucciones alternativas en
# https://github.com/aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE/ Asegúrese de que tiene
# ¡Se han borrado todos los detalles de pago guardados en tu cuenta de Udemy y el navegador!
desde selenium importar webdriver

desde la configuración principal de importación
desde core.utils importar redeem_courses

settings = Settings()
"""### **Introduce la ruta/ubicación de tu webdriver**
De forma predeterminada, el controlador web para el navegador Microsoft Edge ha sido elegido en el siguiente código.

Además, introduzca la ubicación de su conductor web.
"""

# En las ventanas necesita la r (cadena cruda) delante de la cadena para tratar con barras invertidas.
# Reemplaza esta cadena con la ruta de tu webdriver
path = r"..location\msedgedriver.exe"
driver = webdriver.Edge(
    ruta
) # webdriver.Chrome(path) para Google Chrome, webdriver.Firefox(path) para Mozilla Firefox, webdriver.Edge(
# ruta) para Microsoft Edge, webdriver.Safari(path) para Apple Safari

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
