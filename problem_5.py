class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        parent_node = self.root

        for char in word:
            parent_node.insert(char)

            parent_node = parent_node.children[char]
        

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        nodeFind = self.root

        for char in prefix:
            if char not in nodeFind.children:
                return None
            nodeFind = nodeFind.children[char]

        return nodeFind


class TrieNode:
    def __init__(self, value = ''):
        ## Initialize this node in the Trie
        self.value = value
        self.children = {}
        
        
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode(char)
        
    def suffixes(self, suffix = ''):

        suflist = []

        if len(self.children) > 0:

            for child in self.children:

                suflist += self.children[child].suffixes(suffix + child)

            return suflist

        return [suffix]

    

    



MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)



def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print(', '.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print(None)


print("Test 1")    
f('') # return ''

print("\nTest 2")
f('a') # should return: 'nt, nthology, ntagonist, ntogym'

print("\nTest 3")
f('c') # should return "c not found"

print("\nTest 4")
f('anto') # should return "nym"

class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        parent_node = self.root

        for char in word:
            parent_node.insert(char)

            parent_node = parent_node.children[char]
        

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        nodeFind = self.root

        for char in prefix:
            if char not in nodeFind.children:
                return None
            nodeFind = nodeFind.children[char]

        return nodeFind


class TrieNode:
    def __init__(self, value = ''):
        ## Initialize this node in the Trie
        self.value = value
        self.children = {}
        
        
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode(char)
        
    def suffixes(self, suffix = ''):

        suflist = []

        if len(self.children) > 0:

            for child in self.children:

                suflist += self.children[child].suffixes(suffix + child)

            return suflist

        return [suffix]

    

    



MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)



def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print(', '.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print(None)


print("Test 1")    
f('') # return ''

print("\nTest 2")
f('a') # should return: 'nt, nthology, ntagonist, ntogym'

print("\nTest 3")
f('c') # should return "c not found"

print("\nTest 4")
f('anto') # should return "nym"

print("\nTest 5")
f('tri') # should return: 'e, gger, onometry, pod'
