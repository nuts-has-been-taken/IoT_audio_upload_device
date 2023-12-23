import re
from service import DAN, SA

def df_func_name(df_name):
    return re.sub(r'-', r'_', df_name)

def on_register(result):
    func = getattr(SA, 'on_register', None)
    if func: func(result)

IDF_list = getattr(SA,'IDF_list', [])
ODF_list = getattr(SA,'ODF_list', [])
IDF_funcs = {}
for idf in IDF_list:
    IDF_funcs[idf] = getattr(SA, df_func_name(idf), None)
ODF_funcs = {}
for odf in ODF_list:
    ODF_funcs[odf] = getattr(SA, df_func_name(odf), None)

def register():
    device_model = getattr(SA,'device_model', None)
    device_name = getattr(SA,'device_name', None)
    ServerURL = getattr(SA,'ServerURL', None)
    device_id = getattr(SA,'device_id', None)
    if device_id==None: device_id = DAN.get_mac_addr()
    exec_interval = getattr(SA,'exec_interval', 1)
    DAN.profile['dm_name'] = device_model
    DAN.profile['df_list'] = IDF_list + ODF_list  
    if device_name: DAN.profile['d_name']= device_name
    result = DAN.device_registration_with_retry(ServerURL, device_id)
    on_register(result)
