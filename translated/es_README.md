# Inscripción automática de cursos de Udemy: ¡COURSOS PAID GRATIS! (¡Legalmente!)

El código elimina los enlaces y cupones del curso de
[tutorialbar.com](https://tutorialbar.com)

## **_Descargo de responsabilidad y AVISO:_**

1. **IMPORTANT:** Make sure you **clear all saved Debit/Credit Card or any other
   saved payment info from your Browser & your Udemy account** before using the
   script!
2. **Usa** esto SOLO para \*\*propósitos educativos! \* Al usar este código aceptas
   que **no soy responsable de ningún tipo de problema** causado por el código.
3. **Asegúrate de que el raspado de la web sea legal en tu región.**
4. Esto **NO es un script de hacking**, es decir, ¡no puede inscribirte para un curso específico
   ! Instead it finds courses that provide coupon links to make the
   transaction free and then LEGALLY enroll you to the course!

***

## Requisitos:

### ¿Cómo instalar los requisitos?

**Versión de Python requerida:** [Python 3.8+](https://www.python.org/downloads/)

**Debes tener pip instalado. Por favor, busca cómo instalar pip en tu sistema operativo**

Descargue una versión de este proyecto o clone el repositorio y luego vaya a la carpeta
donde haya colocado los archivos. Escribe `pip install -r requirements.txt` para obtener
todos los requisitos instalados de una vez.

- **¡Los controladores web ahora se instalan automáticamente! Pero aquí hay algunos enlaces por si
  estás usando el script vanilla o el navegador Safari:**

* Edge- https\://developer.microsoft.com/es-us/microsoft-edge/tools/webdriver/
* Chrome- https\://chromedriver.chromium.org/
* Firefox- https\://github.com/mozilla/geckodriver/releases/
* Safari-
  https\://developer.apple.com/documentation/webkit/about_webdriver_for_safari/
* Opera- https\://github.com/operasoftware/operachromiumdriver/releases
* Internet Explorer-
  [Encuéntralo por ti mismo](https://www.selenium.dev/downloads/)

**Nota:** Asegúrate de que la versión del controlador coincide con tu navegador.

***

## Instrucciones

1 . Asegúrese de instalar todos los requisitos anteriores.

- Ejecute el script y el cli le guiará a través de la configuración requerida
- De lo contrario, puedes renombrar el siguiente archivo
  [sample_settings.yaml](sample_settings.yaml) a **ajustes. y** y edítala
  usando un editor de texto e inserta tu \*\*correo electrónico registrado de Udemy en la sección
  , tu **contraseña de Udemy en la sección de contraseña**, y el **código postal
  en la sección de código postal (si resides en los Estados Unidos o en cualquier otra región
  donde Udemy solicita el código postal como información de facturación, si no, introduzca un número aleatorio)**.

2 . Elija el archivo apropiado para su navegador (de la lista de abajo):

- **Probado y funciona perfectamente:**

  - Chrome:
    [udemy_enroller_chrome.py](https://github.com/aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE/blob/master/udemy_enroller_chrome.py)
  - Chromium:
    [udemy_enroller_chromium.py](https://github.com/aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE/blob/master/udemy_enroller_chromium.py)
  - Edge:
    [udemy_enroller_edge.py](https://github.com/aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE/blob/master/udemy_enroller_edge.py)

- **Tiene problemas:**

  - Firefox:
    [udemy_enroller_firefox.py(requires manual driver installation)](https://github.com/aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE/blob/master/udemy_enroller_firefox.py)

- **No probado:**

  - Opera:
    [udemy_enroller_opera.py](https://github.com/aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE/blob/master/udemy_enroller_opera.py)

- **Experimentación u otros navegadores (especialmente Safari):**

  - [aka the old bot- requires manual driver setup](https://github.com/aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE/blob/master/udemy_enroller_vanilla.py)

- **Úsalo bajo tu propio riesgo:**
  - Vanilla
  - Explorador de Internet:
    [udemy_enroller_internet_explorer.py](https://github.com/aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE/blob/master/udemy_enroller_internet_explorer.py)

3 . Ejecuta el script elegido en el terminal así:
`python udemy_enroller_firefox.py`

4 . El bot comienza a raspar los enlaces del curso de la primera página de **Todos los cursos**
en [Tutorial Bar](https://www.tutorialbar.com/all-courses/page/1) y comienza
inscríbete a cursos de Udemy. Después de que te haya inscrito a cursos desde la primera página
, luego se mueve a la siguiente página de Barra Tutorial y el ciclo continúa.

- Detenga el script presionando ctrl+c en la terminal para detener el proceso de inscripción.

***

## FAQs

### 1. ¿Puedo obtener un curso específico de forma gratuita con este script?

Unfortunately no, but let me assure you that you may be lucky enough to get a
particular course for free when the instructor posts it's coupon code in order
to promote it. Además, con el tiempo crearás una biblioteca de cursos ejecutando
el script a menudo y teniendo todos los cursos necesarios en tu colección. In fact,
I made this course after completing a
[Python automation course](https://www.udemy.com/course/automate/) and selenium,
which of course I got for free! :)

### 2. ¿Cómo funciona el bot?

El bot recupera los enlaces de cupón de la lista de Tutorial Bar para reducir los precios y
luego utiliza las características de automatización del navegador de Selenium para iniciar sesión y matricularse a los cursos
. Think of it this way: Epic Games & other clients like Steam provide you
a handful of games each week, for free; Only in this case, we need a coupon code
to make those courses free.

### 3. ¿Con qué frecuencia debería ejecutar el script?

¡Diariamente, al menos una vez! Si lo estás usando por primera vez, Recomiendo que
le permita raspar todas las páginas de la barra Tutorial (puede tardar unas horas
ya que hay >500 páginas en el sitio). I've painstakingly amassed over 4000
courses in the last four years! Y de esos 4000, solo he pagado por 4 de
estos cursos.

Así que, ¡un solo **0,001%** de los cursos se **realmente pagan** en mi colección!
¡Afortunadamente, puedes obtener más de lo que recolecté en 4 años, en una cuestión de
semanas! 🙌🏻

### 4. ¿Por qué lo creé?

It used to be my daily habit to redeem courses and it was an extremely tedious
task that took around 15 minutes, for 10 courses. Y entonces de repente tuve la idea
de automatizarlo, después de encontrar el curso de automatización mencionado anteriormente. ¡Apuesto,
te ahorrará tu precioso tiempo también! :)

### 5. ¡Udemy ha detectado que estoy usando herramientas de automatización para navegar por el sitio web! ¿Qué debo hacer?

![](https://i.imgur.com/pwseilE.jpg) Relax! Esto sucede cuando ejecutas el script
varias veces en un corto intervalo de tiempo. Resuelve el captcha, cierra el navegador,
y simplemente vuelve a ejecutar el script. ¡Fácil exprimimiento de limón campesino! 🍋🙃 <br /><br />

### 6. El código se compila con éxito, ¡pero está tardando demasiado en funcionar! ¿Hay alguna forma de arreglarlo?

Puesto que dependemos en gran medida de un sitio de terceros para recuperar enlaces de cupones,
puede haber problemas cuando el sitio está caído. No hace falta mencionar los problemas de conectividad
también. Si todo funciona bien, puedes ver los cursos obtenidos
en la consola/shell de Python, que pueden tardar un tiempo.

### 7. ¿Cuál es la mejor manera de ejecutar el script?

Se recomienda ejecutar el script usando el IDLE IDE de Python.

**Pro-tip:** Crea un archivo batch para ejecutar el script al instante, usando estas instrucciones
: https\://datatofish.com/batch-python-script/

### 8. ¿Qué rama cometer en contra?

Pull request should be made on "develop".

### 9. ¿Cuál es el mapa de ruta?

Echa un vistazo a nuestra
[Hoja de ruta aquí](https://github.com/aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE/projects/1)
y ayúdanos en lo que quieras o habla con nosotros sobre tus cambios propuestos.

***
