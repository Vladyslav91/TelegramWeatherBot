import hvac


VAULT_ADDR = 'http://127.0.0.1:8200'


class VaultService:
    def __init__(self, token):
        self.vault_client = hvac.Client(VAULT_ADDR, token=token)

    def get_secrets(self):
        return self.vault_client.secrets.kv.v2.read_secret_version(path='weatherBot')['data']['data']

    def get_chat_id_secret(self):
        return self.get_secrets()['CHAT_ID']

    def get_api_key_secret(self):
        return self.get_secrets()['API_KEY']

    def get_open_weather_api_key_secret(self):
        return self.get_secrets()['OPEN_WEATHER_API_KEY']
