import os   #libreria para interactuar con el sistema operativo
import openpyxl  #para gestion de documentos tipo xls
import subprocess

# Lista de servidores a los que haremos ping
servidores = ["172.16.11.187","172.16.11.209","172.16.11.135","172.16.11.14","172.16.11.9","172.16.11.223",
                "172.16.11.224","172.16.11.225","172.16.11.226","172.16.11.227",
                "172.16.11.47","172.16.11.48",
                "172.16.11.130",
                "172.16.11.132",
                "172.16.11.60",
                "172.16.11.70",
                "172.16.11.41",
                "172.16.11.91",
                "172.16.11.198",
                "172.16.11.185",
                "172.16.11.186",
                "172.16.11.188",
                "172.16.11.190",
                "172.16.11.164",
                "172.16.11.167",
                "172.16.11.26",#"200.91.239.163"
                "172.16.11.80",
                "172.16.11.113",
                "172.16.11.146",
                "172.16.11.106",
                "172.16.11.11",
                "172.16.11.25",
                "172.16.11.105",
                "172.16.11.149",
                "172.16.11.160",
                "172.16.11.155",
                "172.16.11.170",
                "172.16.11.172",
                "172.16.11.252",
                "172.16.11.182",
                "172.16.11.133",
                "172.16.11.52",
                "172.16.11.53",
                "172.16.11.54",
                "172.16.11.55",
                "172.16.11.57",
                "172.16.11.58",
                "172.16.11.59",
                "172.16.11.183",
                "172.16.11.81",
                "172.16.11.62",
                "172.16.11.222",
                "172.16.11.239",
                "172.16.11.237",
                "172.16.11.238",
                "172.16.11.216",
                "172.16.11.110",
                "172.16.11.192",
                "172.16.11.191",
                "172.16.11.166"] 

# Crear un archivo de Excel para almacenar los resultados
archivo_excel = "resultados ping.xlsx"
libro = openpyxl.Workbook()
hoja = libro.active
hoja.title = "Resultados de Ping"

# Encabezados de la tabla
hoja.append(["Servidor", "Estado"])

# Realizar ping a cada servidor y guardar los resultados
for servidor in servidores:
    try:
        resultado = subprocess.check_output(["ping", "-n", "1", servidor])
        hoja.append([servidor, "Activo"])
    except subprocess.CalledProcessError:
        hoja.append([servidor, "Inactivo"])

# Guardar el archivo de Excel
libro.save(archivo_excel)
print(f"Resultados guardados en {archivo_excel}")
