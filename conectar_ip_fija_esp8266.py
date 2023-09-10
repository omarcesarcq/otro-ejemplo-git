import network

# Nombre de la red Wi-Fi y contraseña
SSID = "HUAWEI_MATE8"
PASSWORD = "d395db00"

# Configura la interfaz Wi-Fi
sta_if = network.WLAN(network.STA_IF)

# Activa la interfaz Wi-Fi
sta_if.active(True)

# Configura una IP estática
sta_if.ifconfig(('192.168.1.100', '255.255.255.0', '192.168.1.1', '8.8.8.8'))

# Conéctate a la red Wi-Fi
sta_if.connect(SSID, PASSWORD)

# Espera a que la conexión se establezca
while not sta_if.isconnected():
    print(".")
    sleep(1)

# Imprime la dirección IP asignada
print("Conectado a la red Wi-Fi")
print("Dirección IP estática: ", sta_if.ifconfig()[0])

