import requests

class NUPNP:
    @staticmethod
    def discover():
        r = requests.get('https://www.meethue.com/api/nupnp')
        return r
