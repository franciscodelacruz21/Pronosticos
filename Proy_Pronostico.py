#Pronosticos
import csv
import datetime as dt
import pandas as pd
import numpy as np
import random


#Lectura de Archivo
df = pd.read_csv("./Chispazo.csv")
df["Llave"] = df[["R1", "R2", "R3", "R4", "R5"]].astype(str).apply(lambda x: "-".join(x), axis =1)
df

TotalConcursos = df.CONCURSO.count()
print(TotalConcursos)

moda = df[["R1","R2","R3","R4","R5"]].mode()
moda["Tipo"] = "Moda"

df_output = pd.DataFrame(moda)
print(df_output)
#df_output 

choice_option = ''

historico_existente = pd.read_excel("Chispazo_Historico_Sugerido.xlsx")

while choice_option != 'y':
 # Generar 5 números aleatorios únicos entre 1 y 28
 combination = random.sample(range(1, 29), 5)

 # Ordenar los números en orden ascendente
 combination.sort()
 separator='-'

 key_lookup = separator.join(map(str,combination))
 #key_lookup = '3-6-9-10-28'

 #Crear un DataFrame con los números
 now = dt.date.today()
 formatted_date = now.strftime("%d/%m/%Y")

 resultado = df[df["Llave"] == key_lookup]

 ncount = len (resultado)


 if ncount == 0:
   print(f"Combinación Sugerida  --> {key_lookup}")

   #Indica si seleccionas la opción
   choice_option = input("Guardar Sugerencia y/n: ")

   historico_existente = pd.read_excel("Chispazo_Historico_Sugerido.xlsx")


   #while choice_option1 != 'y':
   if choice_option == 'y':
      print(f"Evento 1")
      df_sugerencia = pd.DataFrame([combination], columns=['Res1','Res2','Res3','Res4','Res5'])
      df_sugerencia["Fecha"] = formatted_date
      df_sugerencia["Seleccionado"] = choice_option
      print(df_sugerencia)


   elif choice_option != 'y':
      print(f"Evento 2")
      df_sugerencia = pd.DataFrame([combination], columns=['Res1','Res2','Res3','Res4','Res5'])
      df_sugerencia["Fecha"] = formatted_date
      df_sugerencia["Seleccionado"] = choice_option
      print(df_sugerencia)

   #Concatenar Dataframes
   df_combined = pd.concat([historico_existente, df_sugerencia], ignore_index=True)
   #Save the combined data to Excel
   df_combined.to_excel("Chispazo_Historico_Sugerido.xlsx", index=False)


 elif ncount > 0:
    print(f"Combinación Existente:")
    print(resultado)
   
    df_sugerencia = pd.DataFrame([combination], columns=['Res1','Res2','Res3','Res4','Res5'])
    df_sugerencia["Fecha"] = formatted_date
    df_sugerencia["Seleccionado"] = "e"
   
    #Concatenar Dataframes
    df_combined = pd.concat([historico_existente, df_sugerencia], ignore_index=True)

    #Save the combined data to Excel
    df_combined.to_excel("Chispazo_Historico_Sugerido.xlsx", index=False)

    choice_option = 'n'
    print(f"Recalculando......")
   
"""
   while choice_option != 'y':
      print(f"Entra while")

      reloadcombination = random.sample(range(1, 29), 5)
      
      # Ordenar los números en orden ascendente
      reloadcombination.sort()
      separator='-'
      key_lookup_reload = separator.join(map(str,reloadcombination))
      print(key_lookup_reload)
      resultado2 = df[df["Llave"] == key_lookup_reload]
      ncount = len (resultado2)
      print(f"new lookup {ncount}")


      #Indica si seleccionas la opción
      print("Nueva Sugerencia:" + key_lookup_reload)
      choice_option = input("Guardar New Sugerencia y/n: ")

      if choice_option == 'y':
         print(f"Evento 3")
         df_sugerencia = pd.DataFrame([reloadcombination], columns=['Res1','Res2','Res3','Res4','Res5'])
         df_sugerencia["Fecha"] = formatted_date
         df_sugerencia["Seleccionado"] = choice_option
         print(df_sugerencia)

      elif choice_option != 'y':
         print(f"Evento 4")
         df_sugerencia = pd.DataFrame([reloadcombination], columns=['Res1','Res2','Res3','Res4','Res5'])
         df_sugerencia["Fecha"] = formatted_date
         df_sugerencia["Seleccionado"] = choice_option
         print(df_sugerencia)
""" 
  #Save the combined data to Excel
#   df_combined.to_excel("Chispazo_Historico_Sugerido.xlsx", index=False)

