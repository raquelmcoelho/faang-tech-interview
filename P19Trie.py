'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/m23X56ojkYA
Solution: Implement Trie

Trie is a tree-like data structure used to store strings. The tries are also called prefix trees because they provide very efficient prefix matching operations. Implement a trie data structure with three functions that perform the following tasks:

  Insert a string.
  Search a string.
  Search for a given prefix in a string.

Time complexity
Insert(): The time complexity is O(l), where l is the length of the word being inserted.
Search(): The time complexity is O(l), where l is the length of the word that we need to search in the trie.
Search prefix(): The time complexity is O(l), where l is the length of the prefix that we need to search in the trie.

Space complexity
Insert(): The space complexity is O(l) because, in the worst case, we will add l nodes in the trie.
Search(): The space complexity is O(1) because constant space is used while searching the trie.
Search prefix(): The space complexity is O(1) because constant space is used while searching the trie.

'''

class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

def print_with_markers(word, indx):
    out = ""
    for i in range(len(word)):
        if i == indx:
            out += '«'
            out += word[i] + '» '
        else:
            out += word[i] + ' '
    return out


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def print_state(self):
        def recur(node, indent):
            return "".join(indent + key + ("*" if child.is_word else "")
                                  + recur(child, indent + "  ")
                           for key, child in node.children.items())

        return recur(self.root, "\n\t\t\t")

    # inserting string in trie
    def insert(self, word):
        node = self.root
        # adding string characters in the tree
        print("\n\tIserting string in trie")
        j = 0
        for c in word:
            print("\tLoop index ", j, sep="")
            print("\t\t", print_with_markers(word, j), sep="")
            j += 1
            print("\t\tcharacter: ", c, sep="")
            if c not in node.children:
                print("\t\t\t", c, " is not in the trie, creating a new node", sep="")
                node.children[c] = TrieNode()
            else:
                print(
                    "\t\t\t", c, " is already in the trie, hence we move to the next character", sep="")
            print("\t\t\tCurrent state of trie")
            print(self.print_state())
            # update the node as we move to the next character
            node = node.children.get(c)
        print("\n\t\t\tThe word is complete, setting the is_word variable to true")
        node.is_word = True  # set is_word as true when all the string characters have been added
        print("\t\t\t\tis_word: ", node.is_word, sep="")
        print(self.print_state())

    # searching for a string
    def search(self, word):
        print("\n\tSearching for a string")
        node = self.root
        j = 0
        # iterate over the string characters and check in the node's children
        for c in word:
            print("\tLoop index ", j, sep="")
            print("\t\t", print_with_markers(word, j), sep="")
            print("\t\tcharacter: ", c, sep="")
            if j == 0:
                print("\t\tRoot's children: ", node.children.keys())
            else:
                print("\t\tNode ", word[j-1], "'s children: ",
                      node.children.keys(), sep="")
            if c not in node.children:
                print("\t\tCharacter '", c,
                      "' is not present in the node's children, returning False", sep="")
                return False
            else:
                print("\t\tCharacter '", c,
                      "' is present in the node's children, moving to the next character.", sep="")
            # update the node since as we're moving to the next character
            node = node.children.get(c)
            j += 1
        if node.is_word:
            print("\tAll characters are present in the trie and is_word: ",
                  node.is_word, sep="")
            print("\tWord found!")
        else:
            print("\tAll characters are found, however, is_word: ",
                  node.is_word, sep="")
            print("\tWord not found!")
        return node.is_word  # if is_word is true, the string exists

    # searching for a prefix

    def search_prefix(self, prefix):
        print("\n\tSearching for a prefix")
        node = self.root
        j = 0
        # iterate over the string characters and check in the node's children
        for c in prefix:
            print("\tLoop index ", j, sep="")
            print("\t\t", print_with_markers(prefix, j), sep="")
            print("\t\tcharacter: ", c, sep="")
            if j == 0:
                print("\t\tRoot's children: ", node.children.keys())
            else:
                print(
                    "\t\tNode ", prefix[j-1], "'s children: ", node.children.keys(), sep="")
            if c not in node.children:
                print("\t\tCharacter '", c,
                      "' is not present in the node's children, returning False", sep="")
                return False
            else:
                print("\t\tCharacter '", c,
                      "' is present in the node's children, moving to the next character.", sep="")
            # update the node since as we're moving to the next character
            node = node.children.get(c)
            j += 1
        print("\tPrefix found!")
        return True


# Driver Code
def main():
    keys = ["the", "a", "there", "answer"]
    trie_for_keys = Trie()
    num = 1
    for x in keys:
        print(num, ".\tInserting key: ", x, sep="")
        trie_for_keys.insert(x)
        num += 1
        print("-"*100, "\n", sep="")

    search = ["a", "answer", "xyz", "an"]
    for y in search:
        print(num, ".\tSearching key: ", y, sep="")
        print("\t", trie_for_keys.search(y), sep="")
        num += 1
        print("-"*100, "\n", sep="")

    searchPrefix = ["b", "an"]
    for z in searchPrefix:
        print(num, ".\tSearching prefix: ", z, sep="")
        print("\t", trie_for_keys.search_prefix(z), sep="")
        num += 1
        print("-"*100, "\n", sep="")


if __name__ == "__main__":
    main()
