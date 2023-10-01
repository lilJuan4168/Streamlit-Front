import urllib3

def search_products(token:str, word:str):
    headers = {
    "Authorization": f"Bearer {token}"
    }
    new_word = word.strip().replace(" ","%")
    http = urllib3.PoolManager()
    items = http.request("GET",url = f"https://api.mercadolibre.com/sites/MLA/search?q={new_word}", headers=headers)
    return items.json()
#x = search_products("APP_USR-3750359463586153-093013-74f30a003501175650feeb53496be82f-142830670", "Motorola%Moto E13 64gb 2gb%Ram%Azul%Turquesa")
#print(x)
#print(x['paging']['total'])
#print(x['results'][0])