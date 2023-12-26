ServerURL = 'https://class.iottalk.tw' #For example: 'https://iottalk.tw'
MQTT_broker = None # MQTT Broker address, for example:  'iottalk.tw' or None = no MQTT support
MQTT_port = 5566
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'Music_to_Video'
IDF_list = ['MP3_I']
ODF_list = []
device_id = '31283301712261323' #if None, device_id = MAC address
device_name = 'recorder'
exec_interval = 1  # IDF/ODF interval

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

def MP3_I(data):
    return data
