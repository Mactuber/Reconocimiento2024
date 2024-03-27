#Comunmente la mayoría de las máquinas en un segmento de red aceptan y responden a "pings"

#El comanndo ping se encuentra disponible en múltiples plataformas, tales como linux o windows.

#El comando ping utiliza un protocolo simple para el intercambio de mensajes entre máquinas conocido como ICMP.

#El protocolo ICMP es un protocolo de mensajes que permite saber si una máquina determinada esta disponible o no.

#El comando ping utiliza un mensaje ICMP del tipo ECHO_REQUEST para consultar si una máquina se encuentra activa y en el caso de que dicha máquina conteste con un mensaje ICMP ECHO_REPLY, se entiende que la máquina esta activa.

#ICMP es un protocolo de la capa de enlace, por lo tanto no es común utilizarlo directamente por las aplicaciones, pero el comando ping es una clara excepción a la regla.

#Se trata de un protocolo muy útil para diagnóstico de errores en la capa de red y que se utiiza en las herramientas tales como TRACEROUTE para el análisis del tráfico de un paquete por los diferentes routers por los que pasa.

#Este protocolo define una lista de mensajes de control para diferentes propósitos, en el caso del comando PING solamente se utilizan los mensajes "Echo Reply " y "Echo request".

from subprocess import Popen, PIPE

# Diccionario para mapear el rango de valores de TTL a sistemas operativos
ttl_os_map = {
    range(62, 68): "Linux/Unix/MacOS",
    range(124, 131): "Windows",
    range(250, 258): "Solaris/AIX",
    range(60, 67): "FreeBSD"
}

# Lista para almacenar las IPs y sistemas operativos detectados
detected_hosts = []

# Escaneo de la red
for ip in range(1, 20): #rango de IPs
    ip_address = '192.168.1.' + str(ip) #cambiar dirección de red.
    subprocess = Popen(['/sbin/ping', '-c', '1', ip_address], stdout=PIPE, stdin=PIPE, stderr=PIPE) #/sbin/ping en MacOS y /bin/ping en UNIX 
    stdout, stderr = subprocess.communicate(input=None)
    
    if b"bytes from " in stdout:
        ttl_index = stdout.find(b"ttl=")
        if ttl_index != -1:
            ttl_value = int(stdout[ttl_index+4:ttl_index+7])  # Obtener el valor TTL
            detected_os = "Desconocido"
            for ttl_range, os in ttl_os_map.items():
                if ttl_value in ttl_range:
                    detected_os = os
                    break
            detected_hosts.append((ip_address, detected_os))

# Imprimir los resultados en dos columnas
for ip, os in detected_hosts:
    print(f"{ip:<15} {os}")


