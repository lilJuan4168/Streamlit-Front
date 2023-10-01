"""import requests
from requests_oauthlib import OAuth2Session

def get_token(app_id, client_secret):

# Configura los valores de tu aplicación OAuth2
    client_id = 'tu_client_id'
    client_secret = 'tu_client_secret'
    authorization_base_url = 'URL_de_autorizacion_de_la_API'
    token_url = 'URL_de_obtencion_de_token_de_la_API'
    redirect_uri = 'URL_de_redireccionamiento'  # Este debe coincidir con el registrado en la configuración de tu aplicación
# Crea una sesión OAuth2
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)

# Obtiene la URL de autorización
    authorization_url, state = oauth.authorization_url(authorization_base_url)
# Imprime la URL de autorización y abre un navegador para iniciar sesión y obtener el código de autorización
    print("Por favor, visita la siguiente URL en tu navegador y autoriza la aplicación:")
    print(authorization_url)

# Ingresa el código de autorización que obtuviste después de la autorización
authorization_response = input("Ingresa el código de autorización: ")

# Intercambia el código de autorización por un token de acceso
token = oauth.fetch_token(
    token_url,
    authorization_response=authorization_response,
    client_secret=client_secret
)

# Realiza una solicitud GET a la API utilizando el token de acceso
api_url = 'URL_de_la_API_a_la_que_quieres_acceder'
response = oauth.get(api_url)

# Verifica si la solicitud fue exitosa y muestra la respuesta
if response.status_code == 200:
    data = response.json()
    print("Respuesta de la API:")
    print(data)
else:
    print("Error al hacer la solicitud a la API:", response.status_code)

# Puedes usar el token para hacer más solicitudes a la API mientras esté válido
# Asegúrate de manejar adecuadamente la renovación del token cuando expire


"""