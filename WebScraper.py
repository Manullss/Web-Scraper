from seleniumbase import Driver  
import pandas as pd    
# openpyxl    //motor  //con openpyxl podemos conectarnos a excel usando python 
#Con este web escraper extraemos el numero de loteria que caio en cierto dia, saltando en pagina por pagina

def extractor(driver,m):   #se encarga de abrir, navergar y extraer los datos de la pagina 
    dias=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    me=("ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic")
    meses={"ene":[31,23,15,7],"feb":[28,20,12,4],"mar":[31,23,15,7],"abr":[30,22,14,6],  #Como la pagina muestra solo 8 datos por pagina daremos navegaremos entre los datos extrayendo de uno en uno
            "may":[31,23,15,7],"jun":[30,22,14,6],"jul":[31,23,15,7],"ago":[31,23,15,7],    #Como la pagina muestra los datos de atras para adelante empezamos a extraer desde los dias 31,30,28 del mes asta llegar a 1, luego saltamos al mes siguiente
            "sep":[30,22,14,6],"oct":[31,23,15,7],"nov":[30,22,14,6],"dic":[31,23,15,7]}
    while m != 0:
        extraidos=[]       #guarda de 28 a 31 numeros
        ms=[]              #dato mes
        di=[]              #dato dia
        extra=[None] * 32  #guarda los datos finales para ser enviados a Dataframe

        for dia in range(4):             #Buscamos los primeros elementos de la pagina y los extraemos
            num=driver.find_elements('span[class="score "]')
            fechas=driver.find_elements('div[class="session-date px-2"]')
            for i in range(8):
                mes=int((fechas[i].text.replace("-",""))[2:])  #una vez extraidos separamos la fecha del dato objetivo
                da=int((fechas[i].text.replace("-",""))[:2])
                nu=int(num[i].text)
                ms.append(mes)   
                di.append(da)
                extraidos.append(nu)  #datos objetivos
            if dia != 3:
                e=me[m-1]       #Extrae el mes actual para enviarlo a la lista     
                driver.click("input#datepicker")
                driver.click(f'//div/ul/li[@data-view="day" and text()={meses[e][dia+1]}]')   #combina texto con atributo
            if dia == 3:        #continuamos al siguiente mes
                e=me[m-2]
                driver.click("input#datepicker")
                driver.click(f'//div/ul/li[@data-view="day" and text()={meses[e][0]}]')
        #-----------------------------Organizador-------------------------------------
        while len(extraidos) < 32: #Si los datos extraidos son menores de 31 añadimos datos vacios asta llegar a 31
            extraidos.append[None]
        while len(di) < 32:   #si los datos son menores a 32 añadimos datos vacios asta llegar a 31
            di.append[None]
        while len(ms) < 32:   #si los datos son menores a 32 añadimos datos vacios asta llegar a 31
            ms.append[None]
        for i in reversed(dias):  #Empezamos por 31 asta llegar a 1  
            try:
                if ms[i] != m-1:  #Guardamos los datos extraidos deacuerdo al dìa que han aparecido
                    for d in di:
                        if d == i:
                            extra[i]=extraidos[d]
            except:
                print("Hubo un ERROR en la (Posicion 3)")
        if len(extra) >= 32:
            extra.pop(31)
            ms.pop(31)
            di.pop(31)
        #------------------------------------------------------------------------
        excel_extraidos(extra,m,dias)    #enviamos los datos extraidos y el mes actual para convertilos a DataFrame excel
        print(f"Mes {m} completado")
        m-=1  #conteo de meses asta llegar a 0, de ahi continuamos al siguiente año 
    print("----Fin de los 12 meses----")
    
def excel_extraidos(extraidos,m,dias):  #Añadimos los Datos extraidos al archivo excel por medio de la libreria pandas
    mes=["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"]
    df=pd.DataFrame({"Dia":dias,f"{mes[m-1]}":[extraidos]}).set_index("Dia") 
    print(df)
    if m == 1:
        espacio=[None]*31  
        df=pd.DataFrame({"Dia":dias,"-":[espacio]}).set_index("Dia")
        df.to_excel('C:/Users/MA7/Desktop/DiariaDatos9pm.xlsx',index=False,engine='openpyxl') 

#---------------------INICIO---------------------
driver=Driver(uc=True)
#años=["2023","2022","2021","2020","2019","2018","2017","2016","2015","2014","2013","2012"] #Años a extraer
años=[2023] 
for i in años:
    try:
        driver.get(f"https://loteriasdehonduras.com/loto-hn/la-diaria-9pm?date=31-12-{i}")
        extractor(driver,m=12)  #Empezamos por el mes 12 asta llegar al mes 1, luego cambiamos de año y repetimos el siclo asta finalizar la lista años[]
        driver.quit()  
        input("Transición Exitosa   PRESIONA ENTER")
    except:
        print(f"Ocurrio un ERROR en el año {i} (Posicion 1)") 
        continue #aun que halla algun error continuamos a los siguientes años
print("Fin de la transicion") 

