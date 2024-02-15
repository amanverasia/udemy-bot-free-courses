importar getpass
importar os.path
desde distutils.util importar strtobool
desde el escribir importar Dict
desde la lista de importación

desde el volcado de importación de ruamel.yaml
desde ruamel.yaml importar YAML


configuración de clase:
    """
    Contiene toda la lógica relacionada con la configuración de scripts
    """

    def __init__(self):
        self.email = Ninguno
        self.password = Ninguno
        self.zip_code = Ninguno
        self.languages = []

        self._settings_path = "settings.yaml"
        self.is_ci_build = strtobool(os.environ.get("CI", "False"))
        self._init_settings()

    def _init_settings(self) -> Ninguno:
        """
        Inicializar la configuración a usar en el script

        :return:
        """
        if self.is_ci_build:
            self._load_ci_settings()
        no:
            settings = self._load_user_settings()
            si la configuración no es ninguna:
                auto._generar_configuración()
                self._save_settings()

    def _load_ci_settings(self):
        """
        Cargar variables de entorno para ejecutar CI

        :return:
        """
        print("Cargando ajustes de IC")
        self.email = os.environ["UDEMY_EMAIL"]
        self.password = os.environ["UDEMY_PASSWORD"]

    def _load_user_settings(self) -> Dictar:
        """
        Carga la configuración desde el archivo yaml si existe

        Diccionario :return: que contiene la configuración del script
        """
        yaml = YAML()

        ajustes = Ninguno
        si os.path.isfile(self._settings_path):
            print("Cargando ajustes existentes")
            con open(self._settings_path) como f:
                ajustes = yaml.load(f)
            udemy_settings = ajustes["udemy"]
            self.email = configuración de udemy["email"]
            self.password = configuración de udemy["contraseña"]
            self.zip_code = udemy_settings.get("zipcode")
            self.languages = udemy_settings.get("idiomas")
        regresar ajustes

    def _generate_settings(self) -> Ninguno:
        """
        Generar la configuración del script

        :return:
        """
        self.email = self._obtener_email()
        self.password = self._get_password()
        self.zip_code = self._get_zip_code()
        self.languages = self._get_languages()

    def _get_email(self) -> str:
        """
        Obtener entrada del usuario en el correo electrónico para usar para udemy

        :return: El correo udemy de los usuarios
        """
        email = input("Por favor, introduce tu dirección de correo electrónico de udemy: ")
        if len(email) == 0:
            print("Debes proporcionar tu correo electrónico")
            devolver self._get_email()
        correo de devolución

    def _get_password(self) -> str:
        """
        Obtener entrada del usuario en la contraseña para usar para udemy

        :return: La contraseña udemy de los usuarios
        """
        password = getpass.getpass(prompt="Por favor, introduzca su contraseña de udemy: ")
        if len(contraseña) == 0:
            print("Debe proporcionar su contraseña")
            devolver self._get_password()
        devolver contraseña

    @staticmethod
    def _get_zip_code() -> str:
        """
        Obtener entrada del usuario en el código postal para usar para udemy

        :return: El código postal de los usuarios
        """
        zip_code = input(
            "Por favor, introduzca su código postal (no necesario en algunas regiones): ")
        devolver código postal

    @staticmethod
    def _get_languages() -> Lista:
        """
        Obtén información del usuario sobre los idiomas en los que quiere obtener los cursos

        Lista :return: de idiomas en los que el usuario quiere canjear cursos de udemy
        """
        idiomas = entrada(
            "Por favor, introduzca sus preferencias de idioma (lista separada por comas por ejemplo, Inglés, Alemán): "
        )
        return [lang.strip()
                for lang in languages.split(",")] if languages else []

    def _save_settings(self) -> Ninguno:
        """
        Confirmar si el usuario quiere guardar la configuración en el archivo

        :return:
        """
        yaml_structure = dict()
        save_settings = entrada(
            "Desea guardar la configuración para uso futuro (S/N): ")
        if save_settings.lower() == "y":
            yaml_structure["udemy"] = {
                "email": str(self.email),
                "contraseña": str(self.password),
                "zipcode": str(self.zip_code),
                "languages": self.languages,
            }

            con open(self._settings_path, "w+") como f:
                dump(yaml_structure, stream=f)
            imprime(f"Guardado tus ajustes en {self._settings_path}")
        no:
            print("No se guardan los ajustes como se solicita")
