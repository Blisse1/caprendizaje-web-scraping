## Caprendizaje Web Scrapper

## Cómo usar el script
- Instalar pipenv: https://pipenv.pypa.io/en/latest/installation.html
- Sobre la carpeta donde está el script ejecutar:
```bash
$ pipenv shell
$ pipenv install
```
- Crear un archivo .env y colocar sus credenciales de login guiándose del .env.example
- Importante en la variable de entorno de CAPRENDIZAJE_URL_WEB colocar el link que aparece cuando entran a la pagina sin loguearse.
- Ejecutar el script bajo el siguiente comando:
```bash
$ pipenv run python caprendizaje_web_scrape.py
```
- Revisar el archivo empresas.txt creado en la carpeta 

**Nota:** <br>
_Este ejercicio de web scraping se realiza exclusivamente con fines académicos.
El objetivo es únicamente educativo, sin intención de infringir derechos de propiedad intelectual o 
afectar el funcionamiento de las plataformas consultadas._ <br>
**Nota II:** <br>
_El scraping está solo para las empresas de la ciudad de Bogotá_
