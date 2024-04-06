class TextNotionBlock:
    """
    ** color example **
    - "blue"
    - "blue_background"
    - "brown"
    - "brown_background"
    - "default"
    - "gray"
    - "gray_background"
    - "green"
    - "green_background"
    - "orange"
    - "orange_background"
    - "yellow"
    - "green"
    - "pink"
    - "pink_background"
    - "purple"
    - "purple_background"
    - "red"
    - "red_background"
    - "yellow_background"
    """
    def __init__(self, type: str, content: str, color: str='default'):
        self._type = type
        self._content = content
        self._color = color
    
    @property
    def to_dict(self):
        return {
            "object": "block",
            "type": self._type,
            self._type: {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": self._content
                        }
                    }
                ],
                "color" : self._color
            }
        }

class ParagraphBlock(TextNotionBlock):
    def __init__(self, content, color='default'):
        super().__init__("paragraph", content, color)

class Heading1Block(TextNotionBlock):
    def __init__(self, content, color='default'):
        super().__init__("heading_1", content, color)

class Heading2Block(TextNotionBlock):
    def __init__(self, content, color='default'):
        super().__init__("heading_2", content, color)

class Heading3Block(TextNotionBlock):
    def __init__(self, content, color='default'):
        super().__init__("heading_3", content, color)

class QuoteBlock(TextNotionBlock):
    def __init__(self, content, color='default'):
        super().__init__("quote", content, color)