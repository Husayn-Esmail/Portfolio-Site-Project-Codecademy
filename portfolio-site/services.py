import os
import unittest


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

# def read_files():
#     # lists all the subfolders in img folder.
#     files = []
#     img_path = './static/img'

#     try:
#         main_folders = os.listdir(img_path)
#         # cascading path additions
#         paths = DoubleLinkedList(None, None)
#         new_paths = []
#         for folder in main_folders:
#             new_paths.append(img_path+'/%s' % folder)
#         print(new_paths)
#     except NotADirectoryError:
#         # if not a directory use the previous path
#         files = os.listdir('')
#     print(main_folders)
#     """
#     We want to do the following:
#     go through each folder recursively,
#     while entering each folder, store the name of said folder,
#     structure should be as such anyways
#     img
#     --c
#     -final grade calculator
#         - image 1
#         - image 2
#         - image 3
#     - another c project
#         -image 1
#         -image 2
#     -- python
#     - html api
#         -image 1
#         -image 2
#     ...
#     so at most it should be only going 2 directories deep. 
#     """        

def read_images(path: str):
    """
    Gets all the folders in a given path and traverses one level down to obtain
    all the filenames within the folders of that path. Stores the contents of
    each folder next to the folder name in a dictionary.
    returns the dictionary
    """
    outer_directories = os.listdir(path)
    images = {}
    for directory in outer_directories:
        if directory == 'favicons':
            continue
        temp_path = path + '/' + directory
        images[directory] = os.listdir(temp_path)
    return images



if __name__ == '__main__':
    path = "./static/img"
    print(read_images(path))
    unittest.main()
    

