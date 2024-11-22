import network
import firebase
import openweathermap as weather
import time
import gc
import random

GLOB_WLAN = network.WLAN(network.STA_IF)
GLOB_WLAN.active(True)
GLOB_WLAN.connect("Guardachuva_2G", "@Quinta06Feira#")
#GLOB_WLAN.connect("Sala_2.4G", "522FBDB710")

count = 0
while not GLOB_WLAN.isconnected():
    time.sleep(1)
    count += 1
    print(count)
    pass

while 1:
    time.sleep(5)
    gmtime = list(map(str, time.gmtime()))
    dia = ('00' + gmtime[2])[-2:]
    mes = ('00' + gmtime[1])[-2:]
    ano = gmtime[0]
    hora = ('00' + gmtime[3])[-2:]
    minuto = ('00' + gmtime[4])[-2:]
    segundo = ('00' + gmtime[5])[-2:]
    timestamp = f"{dia}_{mes}_{ano}-{hora}_{minuto}_{segundo}"
    print("Timestamp:", timestamp)
    #sensor_manager = senman.SensorsManager()
    weather_data = weather.get_weather_data()
    sensor_data = {"temperatura": random.uniform(20.00,36.00), "umidade": random.uniform(60.00,64.00), "som": 2, "pressao": random.uniform(930.00,940.00)}
    dados = None
    dados = {"sensor": sensor_data, "openweathermap": weather_data}
    dados = {timestamp: dados}
    firebase.patch_data(dados)
    mem_info = gc.mem_free(), gc.mem_alloc()
    print("Memória livre: {} bytes".format(mem_info[0]))
    print("Memória alocada: {} bytes".format(mem_info[1]))
    gc.collect()