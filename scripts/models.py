class SearchRequest:
    def __init__(self, id, request, channel_id):
        self.id = id
        self.request = request
        self.channel_id = channel_id


class ItemShowed:
    def __init__(self, name, url):
        self.name = name
        self.url = url