class Trie:

    def __init__(self):
        self.ls = [[]]

    def insert(self, word: str) -> None:
        self.ls.append([word])
    
    def search(self, word: str) -> bool:
        if [word] in self.ls:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        length = len(prefix)
        for s in self.ls[1:]:
            if (len(s[0]) >= length) and (prefix == s[0][:length]):
                return True
        else:
            return False