class Trie:

    def __init__(self):
        self.text = [[]]

    def insert(self, word: str) -> None:
        self.text.append([word])

    def search(self, word: str) -> bool:
        if [word] in self.text:
            return True
        else :
            return False

    def startsWith(self, prefix: str) -> bool:
        for char in self.text[1:]:
            if char[0][:len(prefix)]==prefix:
                return True
        return False