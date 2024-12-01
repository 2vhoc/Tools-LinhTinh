import pyshorteners as ps
class short:
    def __init__(self, Link):
        self.Link = Link
    def run(self):
        typeTiny = ps.Shortener()
        shortLink = typeTiny.tinyurl.short(self.Link)
        return shortLink
