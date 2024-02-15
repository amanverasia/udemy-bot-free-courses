importar subproceso
importar sys
importar os

instalación def (paquete):
    #subprocess.check_call([sys.executable, "-m", "pip", "install", str(package)])
    os.system("pip install "+ str(package))
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'show', str(package)])

    print(str(reqs) + "\n")
    print("Installed " + package.upper() + "\n")

instalación("peticiones")
install("Beaufulsoup4")
install("ruamel.yaml")
install("selenium")
install("webdriver_manager")