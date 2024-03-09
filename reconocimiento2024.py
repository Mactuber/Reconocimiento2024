import re
import nmap
import os

def validar_direccion_ip(ip):
    # Expresión regular para validar una dirección IP
    patron = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(patron, ip)

def realizar_escaneo(ip):
    nm = nmap.PortScanner()
    resultado = nm.scan(hosts=ip, arguments='-sn')

    hosts_descubiertos = []
    for host in nm.all_hosts():
        hosts_descubiertos.append(host)

    hosts_descubiertos.sort()  # Ordenar las direcciones IP descubiertas

    print("\nHosts descubiertos en la subred:")
    for host in hosts_descubiertos:
        print(host)

    respuesta = input("\n¿Desea realizar un escaneo más concreto a una IP específica? (Si/No): ")
    if respuesta.lower() == "si":
        ip_objetivo = input("Introduce la dirección IP para realizar un escaneo más concreto: ")
        escanear_concreto(ip_objetivo)
    else:
        print("¡Muchas gracias! Que tengas un buen día.")

def escanear_concreto(ip):
    comando_nmap = f"nmap -p- -sS --min-rate 5000 --open -vvv -n -Pn {ip} -oG allPorts"
    print(f"Ejecutando el siguiente comando Nmap para escanear la IP {ip} de forma más concreta:")
    print(comando_nmap)
    os.system(comando_nmap)

    respuesta = input("\n¿Desea obtener mayor información de los servicios detectados? (Si/No): ")
    if respuesta.lower() == "si":
        puertos = obtener_puertos_desde_archivo("allPorts")
        escanear_servicios(ip, puertos)
    else:
        print("Muchas gracias por confiar en nuestro escaneo, te deseo un buen día.")

def obtener_puertos_desde_archivo(archivo):
    puertos = []
    with open(archivo, 'r') as f:
        for linea in f:
            if "Ports:" in linea:
                puertos.extend(re.findall(r"\d+/(?:open|closed)/", linea))
    return puertos

def escanear_servicios(ip, puertos):
    # Filtramos los puertos para asegurarnos de que solo sean los números
    puertos_filtrados = [p.split('/')[0] for p in puertos]
    puertos_str = ",".join(puertos_filtrados)
    
    comando_nmap = f"nmap -sCV -p{puertos_str} {ip} -oN targeted"
    print(f"Ejecutando el siguiente comando Nmap para obtener mayor información de los servicios detectados en la IP {ip}:")
    print(comando_nmap)
    os.system(comando_nmap)

    print("¡El reconocimiento ha sido un éxito!")

def main():
    while True:
        direccion_ip = input("Por favor, introduce una dirección de red para escanear (formato xxx.xxx.xxx.xxx): ")

        if validar_direccion_ip(direccion_ip):
            realizar_escaneo(direccion_ip)
            break
        else:
            print("La dirección IP ingresada no es válida. Por favor, inténtalo de nuevo.")

if __name__ == "__main__":
    main()
