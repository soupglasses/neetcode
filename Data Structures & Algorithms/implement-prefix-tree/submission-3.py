from dataclasses import dataclass

@dataclass
class TrieNode:
    terminating: bool
    decendants: dict["str", "TrieNode"]


class PrefixTree:

    def __init__(self):
        self.sentinel: TrieNode = TrieNode(False, dict())

    def insert(self, word: str) -> None:
        node = self.sentinel
        for char in word:
            child_node = node.decendants.get(char)
            if child_node is None:
                child_node = TrieNode(False, dict())
                node.decendants[char] = child_node
            node = child_node
        node.terminating = True

    def search(self, word: str) -> bool:
        node = self.sentinel
        for char in word:
            node = node.decendants.get(char)
            if node is None:
                return False
        return node.terminating

    def startsWith(self, prefix: str) -> bool:
        node = self.sentinel
        for char in prefix:
            node = node.decendants.get(char)
            if node is None:
                return False
        return True
        