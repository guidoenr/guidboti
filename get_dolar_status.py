import json
import logging
from datetime import time

import requests, constants

def get_principal_values():
    try:
        response = requests.request('GET', constants.URI_DOLARSI)
    except:
        logging.warning("the URI: " + constants.URI_DOLARSI + " seems to be down, trying again")
        time.sleep(2)
        # TODO
    finally:
        return response.json()


def get_dolar_mep(json_response):
    input_dict = json.loads(json_response)
    output_dict = [x for x in input_dict if x['nombre'] == 'Dolar Bolsa']
    output_json = json.dumps(output_dict)
    return output_json['compra'], output_json['venta']


if __name__ == '__main__':
    respones = get_principal_values()
    asd = get_dolar_mep(respones)