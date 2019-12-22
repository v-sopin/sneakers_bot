class SearchRequest:
    def __init__(self, id, request, channel_id, type):
        self.id = id
        self.request = request
        self.channel_id = channel_id
        self.type = type


class ItemShowed:
    def __init__(self, name, url, request_id):
        self.name = name
        self.url = url
        self.request_id = request_id
