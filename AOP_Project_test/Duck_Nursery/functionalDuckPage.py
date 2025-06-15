from page import Page

class FunctionalDuckPage(Page):
    comment = ""
    
    def __init__(self, duckVariety, comment=""):
        self.category = "Functional Duck"
        self.duckVariety = duckVariety
        self.comment = comment
    