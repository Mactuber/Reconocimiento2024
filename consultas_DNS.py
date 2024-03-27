import dns.resolver
import dns.name
import dns.reversename

def print_dns_info(domain):
    print("Información del servidor DNS para el dominio:", domain)
    print("---------------------------------------------\n")

    # Registros A: Resuelve nombres de host a direcciones IPv4
    ansA = dns.resolver.resolve(domain, 'A')
    print("Registros A:")
    for answer in ansA:
        print(answer.address)

    # Registros AAAA: Resuelve nombres de host a direcciones IPv6
    ansAAAA = dns.resolver.resolve(domain, 'AAAA')
    print("\nRegistros AAAA:")
    for answer in ansAAAA:
        print(answer.address)

    # Registros MX: Resuelve el nombre del servidor de correo para el dominio
    ansMX = dns.resolver.resolve(domain, 'MX')
    print("\nRegistros MX:")
    for answer in ansMX:
        print(answer.preference, answer.exchange)

    # Registros TXT: Proporciona texto arbitrario asociado con el nombre de dominio
    ansTXT = dns.resolver.resolve(domain, 'TXT')
    print("\nRegistros TXT:")
    for answer in ansTXT:
        print(answer)

    # Registros SOA: Proporciona información de autoridad sobre la zona DNS
    ansSOA = dns.resolver.resolve(domain, 'SOA')
    print("\nRegistros SOA:")
    for answer in ansSOA:
        print(answer)

    # Información de dominio y subdominios
    print("\nInformación de dominio y subdominios:")
    n = dns.name.from_text('www.' + domain)
    n1 = dns.name.from_text(domain)
    print("¿Es www." + domain + " un subdominio de " + domain + "?:", n.is_subdomain(n1))
    print("¿Es " + domain + " un subdominio de www." + domain + "?:", n1.is_subdomain(n))
    print("Relativizar www." + domain + " respecto a " + domain + ":", n.relativize(n1))
    print("Etiquetas de www." + domain + ":", n.labels)
    print("Etiquetas de " + domain + ":", n1.labels)

    # Consulta inversa para 127.0.0.1
    print("\nConsulta inversa para 127.0.0.1:")
    n = dns.reversename.from_address('127.0.0.1')
    print(n)
    print("Dirección asociada:", dns.reversename.to_address(n))

# Solicitar al usuario el dominio de interés
domain = input("Por favor, introduce el nombre de dominio que deseas consultar: ")

# Llamada a la función para generar el informe
print_dns_info(domain)
