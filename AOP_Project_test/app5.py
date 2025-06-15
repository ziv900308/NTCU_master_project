from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def show(self):
        pass

class DocumentCreator(ABC):
    @abstractmethod
    def createDocument(self) -> Document:
        pass

class TextDocument(Document):
    def show(self):
        print("This is a TextDocument.")

class DrawingDocument(Document):
    def show(self):
        print("This is a DrawingDocument.")

class TextDocumentCreator(DocumentCreator):
    def createDocument(self) -> Document:
        return TextDocument()

class DrawingDocumentCreator(DocumentCreator):
    def createDocument(self) -> Document:
        return DrawingDocument()

class Application:
    @staticmethod
    def createDocument(filetype: str):
        creator: DocumentCreator
        if filetype == "text":
            creator = TextDocumentCreator()
        elif filetype == "draw":
            creator = DrawingDocumentCreator()
        else:
            print("Unknown file type.")
            return
        doc = creator.createDocument()  # Java-style
        doc.show()

Application.createDocument("text")
Application.createDocument("draw")