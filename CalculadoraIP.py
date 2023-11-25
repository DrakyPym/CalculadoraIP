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

direccion_ip_usuario = input("Ingrese una dirección IP: ")
mascara_usuario = input("Ingrese la máscara de red: ")

obtener_informacion_red(direccion_ip_usuario, mascara_usuario)
