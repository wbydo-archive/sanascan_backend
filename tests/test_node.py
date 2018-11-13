import unittest

from sanascan_backend.node import Node, RootNode, EOSNode
from sanascan_backend.word import Word


class TestNode(unittest.TestCase):
    def setUp(self) -> None:
        self.hoge_word = Word(surface='歩下', yomi='ホゲ')
        self.node = Node(self.hoge_word)
        self.root = RootNode()
        self.eos = EOSNode()

    def test_init(self) -> None:
        with self.subTest():
            self.assertEqual(self.node._word, self.hoge_word)

        with self.subTest():
            w = Word(surface='<s>', yomi='<s>')
            self.assertEqual(self.root._word, w)

        with self.subTest():
            w = Word(surface='</s>', yomi='</s>')
            self.assertEqual(self.eos._word, w)


if __name__ == '__main__':
    unittest.main()
