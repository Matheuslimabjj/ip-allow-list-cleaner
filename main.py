def update_file(import_file, remove_list):
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    ip_addresses = ip_addresses.split()

    for element in remove_list:
        if element in ip_addresses:
            ip_addresses.remove(element)

    ip_addresses = "\n".join(ip_addresses)

    with open(import_file, "w") as file:
        file.write(ip_addresses)

# Executar função com lista de IPs a serem removidos
update_file("allow_list.txt", ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"])

# Debug: verificar conteúdo atualizado
with open("allow_list.txt", "r") as file:
    text = file.read()

print(text)
