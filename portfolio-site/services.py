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
        pass

    def test_node_get_next(self):
        pass

    def test_node_set_next(self):
        pass

    def test_node_get_prev(self):
        pass

    def test_node_set_prev(self):
        pass
    
    def test_node_get_data(self):
        pass

    def test_node_set_data(self):
        pass

def read_files():
    # lists all the subfolders in img folder.
    files = []
    img_path = './static/img/python'
    try:
        main_folders = os.listdir(img_path)
        # cascading path additions
        new_paths = []
        for folder in main_folders:
            new_paths.append(img_path+'/%s' % folder)
        print(new_paths)
    except NotADirectoryError:
        # if not a directory use the previous path
        files = os.listdir('')
    print(main_folders)
    """
    We want to do the following:
    go through each folder recursively,
    while entering each folder, store the name of said folder,
    structure should be as such anyways
    img
    --c
    -final grade calculator
        - image 1
        - image 2
        - image 3
    - another c project
        -image 1
        -image 2
    -- python
    - html api
        -image 1
        -image 2
    ...
    so at most it should be only going 2 directories deep. 
    """        

if __name__ == '__main__':
    read_files()
    unittest.main()
    

