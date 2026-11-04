class TriNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class WordDictionary:
    """
    U: We are adding words to our data strucutre and searching for them
    Main problem: if there are dots .ay, b.., .a., we have to replace those with other letters and search if that word exists. in this example, b.., any word that starts with b and has three letters qualify
    M:;
    P: We can use brute force
    We create a trie since trie letss us know if somethiig is follwoing the same path
    We declare trie by
    class TriNode():
        def __init__(self):
            self.children = {}
            self.is_word = False
    
    we use the same way to add word

    node = self.root
    for char in word:
        if not char in node.children:
            node.children[char] = TriNode()
        
        node = node.children[char]
    node.is_word = True

    for search it is little different
    We can use usual search but with a twist
    node = self.root

    for char in word:
        if not char in node.children:
            return False
        node = node.children[char]
    return node.is_word

    but we need to be ware of . so we can probably search in the word
    if . in word:
        #if . is in the start we skil that many root values and mvoe to next one. 
        if . is in the middle we skip tha manh values and move. 
        the idea is simple skip whenver . is there and after skipping and goign through chars in word see if is_word is true or false
    

    """

    def __init__(self):
        self.root = TriNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if not char in node.children:
                node.children[char] = TriNode()
            node = node.children[char]
        
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if len(word) == index:
                return node.is_word
            char = word[index]
            if char == ".":
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True
                return False

            if char not in node.children:
                return False
            
            return dfs(node.children[char], index+1)

        return dfs(self.root, 0)
    
