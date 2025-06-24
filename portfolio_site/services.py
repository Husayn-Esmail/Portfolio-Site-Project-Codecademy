import os
import unittest
from recursive import recursive_indexer
class DoubleLinkedListNode:
    """
    to be used in when recursively searching directories
    """
    def __init__(self, prev, data, next):
        self._prev = prev
        self._data = data
        self._next = next

    def get_prev(self):
        return self._prev

    def get_data(self):
        return self._data
    
    def get_next(self):
        return self._next
    
    def set_prev(self, newPrev):
        self._prev = newPrev

    def set_data(self, newData):
        self._data = newData

    def set_next(self, newNext):
        self._next = newNext
    

class DoubleLinkedList:
    '''
    used to define the overall structure of the double
    linked list
    '''
    def __init__(self, head, tail):
        self._head = head
        self._tail = tail
        self._size = 0
    
    def get_head(self):
        return self._head
    
    def get_tail(self):
        return self._tail

    def append_node(self, node):
        if self._head == None:
            self._head = node
            self._tail = node
            self._size += 1
            return self._head
        node.set_prev(self._tail)
        self._tail.set_next(node)
        self._size += 1
        return self._tail

class TestDLLNode(unittest.TestCase):
    def test_node_creation(self):
        node1 = DoubleLinkedListNode(None, 3, None)
        self.assertIs(type(node1), DoubleLinkedListNode, "node is a node")

    def test_node_get_next(self):
        node1 = DoubleLinkedListNode(None, 2, None)
        node2 = DoubleLinkedListNode(None, 3, node1)
        self.assertEqual(node2.get_next(), node1, "get_next actually gets next")

    def test_node_set_next(self):
        node1 = DoubleLinkedListNode(None, 2, None)
        node2 = DoubleLinkedListNode(node1, 3, None)
        node1.set_next(node2)
        self.assertEqual(node1.get_next(), node2, "check that set_next sets next")

    def test_node_get_prev(self):
        node1 = DoubleLinkedListNode(None, 2, None)
        node2 = DoubleLinkedListNode(node1, 2, None)
        expected = node1
        actual = node2.get_prev()
        self.assertEqual(actual, expected, "get_prev returns previous node")

    def test_node_set_prev(self):
        node1 = DoubleLinkedListNode(None, 2, None)
        node2 = DoubleLinkedListNode(None, 2, None)
        expected = node1
        node2.set_prev(node1)
        actual = node2.get_prev()
        self.assertEqual(actual, expected, "set_prev sets node's previous")
    
    def test_node_get_data(self):
        node1 = DoubleLinkedListNode(None, 3, None)
        expected = 3
        actual = node1.get_data()
        self.assertEqual(actual, expected, "get_data returns value in data")

    def test_node_set_data(self):
        node1 = DoubleLinkedListNode(None, None, None)
        node1.set_data(5)
        expected = 5
        actual = node1.get_data()
        self.assertEqual(actual, expected, "set_data changes the value of data")



if __name__ == '__main__':
    unittest.main()
    

