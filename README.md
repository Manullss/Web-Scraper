## :8ball:Web Scraper – Lotería de Honduras

Este proyecto es un web scraper en Python que extrae los números ganadores de la Lotería de Honduras (La Diaria 9 PM) día por día, mes  por mes y año por año, y los guarda en un archivo Excel.  

El script navega automáticamente por el calendario del sitio web, recorriendo meses y páginas para obtener todos los resultados disponibles.  


https://github.com/user-attachments/assets/a7c10021-8696-4fc5-b44d-dbb680f30a72

🧩 Características  
-Navegación automática con SeleniumBase  
-Extracción de datos por:   
1- Día  
2- Mes  
3- Año  
-Manejo de paginación del calendario  
-Organización de datos por mes  
-Exportación de resultados a Excel  
-Soporte para múltiples años  

🛠️ Requisitos  
-Python 3.9 o superior  
-Google Chrome instalado

### Librerias Necesarias
```
pip install seleniumbase pandas openpyxl
```
> [!NOTE]
> SeleniumBase maneja automaticamente el WebDriver.

### ⚙️ Cómo funciona  
1-Navegación web  
Sabre la página de resultados de la lotería  
Se usa el calendario del sitio para moverse entre días y meses  
El scraper extrae los números ganadores visibles en cada página  


2-Extracción de datos  
Se obtienen:  
-Número ganador  
-Día   
-Mes  
La página muestra solo 8 resultados por vista, por lo que el script navega automáticamente entre fechas anteriores

3-Organización  
Los datos se ordenan del día 31 al 1  
Se rellenan los días sin resultados con valores vacíos (None)   
Cada mes se guarda como una columna en Excel  

4-Exportación a Excel
Se crea un archivo llamado: *Datos9pm.xlsx*   
Cada columna representa un mes  
Las filas representan los días del mes  

La ruta del archivo Excel está definida manualmente y puede ajustarse: *'C:/Users/Desktop/Datos9pm.xlsx'*

📚 Tecnologías usadas
- Python  
- SeleniumBase  
- Pandas  
- OpenPyXL  

El objeto Driver (o driver) es el que controla el navegador.
Cada uno de esos métodos sirve para interactuar con la página web o con el navegador
Algunos elementos usados de esta librería son:  

Driver.click(selector)---------- Hace clic sobre un elemento de la página.  
Driver.find_elements(selector)-- Devuelve una lista de elementos que coinciden con el selector  
Driver.quit()-------------------- Cierra completamente el navegador y termina la sesión  
Driver.get(url)------------------ Carga una URL en el navegador.  
Driver.open(url)---------------- Abre una URL, pero es un método propio de SeleniumBase  

Pandas es una herramienta de análisis y manipulación de datos de código abierto rápida, potente, 
flexible y fácil de usar, ideal para trabajar con archivos como Excel, Csv, Json, etc.
Algunos elementos utilizados de esta librería son: 

pd.DataFrame()        ---- Crear un DataFrame vacío  
df.to_excel(ruta)     ---- Guarda el DataFrame en un archivo Excel (.xlsx)

Autor: >Manuel Edgardo Barahona - Proyecto Educativo
