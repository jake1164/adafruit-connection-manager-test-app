import os
import gc
import ssl
import wifi
import socketpool
import adafruit_requests
import adafruit_connection_manager


ssid = os.getenv('WIFI_SSID')
password = os.getenv('WIFI_PASSWORD')

wifi.radio.connect(ssid, password)

#pool = socketpool.SocketPool(wifi.radio)

ssl_context = adafruit_connection_manager.get_radio_ssl_context(wifi.radio)
pool = adafruit_connection_manager.get_radio_socketpool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl_context)


url = 'https://swd.weatherflow.com/swd/rest/observations/station/52477?token=redacted'

try:
    print(f'getting url: {url}')

    with requests.get(url) as response:
        print(response.json())
except Exception as e:
    print('response.json Exception:', e)

