import requests

# URL de la API de GLPI
url = "http://10.20.10.32/glpi/apirest.php/search/Ticket"

# Parámetros de búsqueda
params = {
    "is_deleted": 0,
    "session_token": "6e6673cad205fee928b650274dfc63db",
    "criteria[0][field]": 1,
    "criteria[0][searchtype]": "contains",
    "criteria[0][value]": "",
    "search": "Rechercher",
    "itemtype": "Ticket",
    "start": 0,
    "criteria[1][link]": "AND",
    "criteria[1][field]": 12,
    "criteria[1][searchtype]": "equals",
    "criteria[1][value]": 1,
    "forcedisplay[0]": 0,
}

# Realizar la solicitud GET a la API de GLPI
response = requests.get(url, params=params)

# Verificar si la solicitud fue exitosa (código de respuesta 200)
if response.status_code == 200:
    # Analizar la respuesta JSON
    data = response.json()
    
    # Obtener el número total de tickets (contador)
    totalcounter = data['totalcount']
    
    print(f"Número total de tickets: {totalcounter}")
else:
    print(f"Error en la solicitud: Código de respuesta {response.status_code}")
