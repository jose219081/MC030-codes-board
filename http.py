import urequests

def http_request(url):
    """Realiza uma requisição HTTP GET."""
    response = urequests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Erro na requisição: {}".format(response.status_code))