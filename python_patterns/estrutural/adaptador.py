class _Telefone:
    def telefonar(self, ddd, numero):
        print(f'ligando para ({ddd}) {numero}')


class _WhatsAppAPI:
    def call(self, phone):
        ''' phone must be on formt +country code and phone number'''
        print('Zap Zap call to {phone}')


class WhatsAppAPIToTelefoneAdapter:
    def __init__(self, whats_api):
        self._whats_api = whats_api

    def telefonar(self, ddd, telefone):
        return self._whats_api.call(f'+55{ddd} {telefone}')


class _TelegramAPI:
    def phone_call(self, country_code, phone):
        ''' phone must be on formt +country code and phone number'''
        print('Telegram phone call to {country_code} {phone}')


class TelegramParaTelefoneAdapterMixin():
    def telefonar(self, ddd, telefone):
        self.phone_call('55', f'{ddd}{telefone}')


class TelegramParaTelefoneAdapter(TelegramParaTelefoneAdapterMixin, _TelegramAPI):
    pass


telefone = TelegramParaTelefoneAdapter()


if __name__ == '__main__':
    # Imagine em mil lugares diferentes, em diferentes pacotes e modulos
    telefone.telefonar('12', '2345678')
    telefone.telefonar('12', '2345678')
