import network
import time

def connect_to_wifi():
    REDE = "Guardachuva_2G"
    SENHA = "@Quinta06Feira#"

    ### Conexão wi-fi, com rede e senha pré-definidos
    GLOB_WLAN = network.WLAN(network.STA_IF)
    GLOB_WLAN.active(True)

    counter = 0
    print("Tentativas de conexão à rede wi-fi", REDE, ":", end='')
    while not GLOB_WLAN.isconnected():
        GLOB_WLAN.connect(REDE, SENHA)
        counter += 1
        print(counter, ", ", end='')
        time.sleep(4)
        pass
    print("Wi-fi Conectado")
    
