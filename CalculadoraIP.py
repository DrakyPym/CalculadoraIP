import ipaddress

def obtener_informacion_red(direccion_ip, mascara):
    try:
        # Crear un objeto de red utilizando ip_network
        red = ipaddress.ip_network(f"{direccion_ip}/{mascara}", strict=False)

        print(f"\nInformación para la red {red}:\n")
        print(f"Dirección de red: {red.network_address}")
        print(f"Máscara de red: {red.netmask}")
        print(f"Wilcard: {red.hostmask}")
        print(f"Cantidad de hosts en la red: {len(list(red.hosts()))}")
        hosts = list(red.hosts())
        print(f"Host mínimo: {hosts[0]}")
        print(f"Host máximo: {hosts[-1]}")
        print(f"Dirección de Broadcast: {red.broadcast_address}")
        
    except ValueError:
        print("¡Dirección IP o máscara de red no válida!")
        
def obtener_subredes(direccion_ip, mascara, nueva_mascara):
    # Crear un objeto de red utilizando ip_network
    red = ipaddress.ip_network(f"{direccion_ip}/{mascara}", strict=False)
    print("###################################################")
    print(f"\nSubredes con la nueva máscara (/{nueva_mascara}):")
    for subred in red.subnets(prefixlen_diff=(int(nueva_mascara) - int(mascara))):
        print(f"\nInformación para la subred {subred}:\n")
        print(f"Dirección de subred: {subred.network_address}")
        print(f"Máscara de subred: {subred.netmask}")
        print(f"Wilcard: {subred.hostmask}")
        print(f"Cantidad de hosts en la subred: {len(list(subred.hosts()))}")
        hosts = list(subred.hosts())
        print(f"Host mínimo: {hosts[0]}")
        print(f"Host máximo: {hosts[-1]}")
        print(f"Dirección de Broadcast: {subred.broadcast_address}")

def decimal_a_binario(decimal):
    if decimal < 0:
        return "No se admiten números negativos en la dirección IP"
    elif decimal == 0:
        return "0"
    else:
        binario = bin(decimal)[2:]  # Elimina los primeros dos caracteres "0b"
        return str(binario)

direccion_ip_usuario = input("Ingrese una dirección IP: ")
mascara_usuario = input("Ingrese la máscara de red: ")

obtener_informacion_red(direccion_ip_usuario, mascara_usuario)

nueva_mascara = input("\nIngrese la nueva mascara para calcular las subredes: ")
obtener_subredes(direccion_ip_usuario, mascara_usuario, nueva_mascara)
