class ApDto:

    def __init__(self, html):
        self.id = ''
        self.html = html
        self.cod = 0
        self.title = ''
        self.detail = ''
        self.category = ''
        self.region = ''
        self.price = 0
        self.seller = ''
        self.phone = ''
        self.email = ''
        self.dateInsert = ''
        self.url = ''
        self.cep = ''
        self.city = ''
        self.neighbourhood = ''
        self.address = ''
        self.location = ''
        self.description = ''
        self.image = ''
        self.uf = ''

    def get_id(self):
        return self.id


