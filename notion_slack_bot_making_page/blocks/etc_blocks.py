class DividerNotionBlock:
    def __init__(self):
        self._type = "divider"
    
    @property
    def to_block(self):
        return [{
            "object": "block",
            "type": self._type,
            self._type: {}
        }]

class ImageNotionBlock:
    def __init__(self, image_url):
        self._type = "image"
        self._image_url = image_url

    @property
    def to_block(self):
        return [{
            "object": "block",
            "type": self._type,
            self._type: {
                "type": "external",
                "external": {
                    "url": self._image_url
                }
            }
        }]