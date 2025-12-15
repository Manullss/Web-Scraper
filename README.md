Para este proyecto utilizamos las librerías SeleniumBase, Pandas y Pytest, 
SeleniumBase - SeleniumBase es un framework de automatización de navegadores con el que 
podemos trabajar con páginas web, añadiendo, extrayendo, navegando, entre muchas otras cosas más, es 
ideal para este proyecto de web scraping.

El objeto Driver (o driver) es el que controla el navegador.
Cada uno de esos métodos sirve para interactuar con la página web o con el navegador
Algunos elementos usados de esta librería son:

Driver.click(selector) 			    # Hace clic sobre un elemento de la página.
Driver.find_elements(selector)	# Devuelve una lista de elementos que coinciden con el selector
Driver.quit()    	              # Cierra completamente el navegador y termina la sesión
Driver.get(url)				          # Carga una URL en el navegador.
Driver.open(url)  	            # Abre una URL, pero es un método propio de SeleniumBase		

Pandas - Pandas es una herramienta de análisis y manipulación de datos de código abierto rápida, potente, 
flexible y fácil de usar, 
ideal para trabajar con archivos como Excel, Csv, Json, etc.
Algunos elementos utilizados de esta librería son: 

pd.DataFrame()	    # Crear un DataFrame vacío
df.to_excel(ruta)	  # Guarda el DataFrame en un archivo Excel (.xlsx)

Pytest– Necesitamos pytest para trabajar con Selenium pues con este podemos ejecutar el código con la consola de comando, 
para llamar a este Framework escribimos pytest -q Nombre_del_Programa.py en la consola y ejecutara el web scraper 
Para ejecutarlo con pytest, en la consola colocamos test_ atrás del nombre del programa, ejemplo pytest test_Escraper.py, 
si no se coloca el test el programa no se ejecutará
