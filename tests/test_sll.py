import pytest
from recursive import recursive_indexer

class TestSll:
    def setup(self):
        self.data = "some data"
        self.sls = recursive_indexer.sll(self.data)
    
    def test_get_data(self):
        assert self.sls.get_data() == self.data
    
    def test_set_data(self):
        data = "new data"
        self.sls.set_data(data)
        assert self.sls.get_data() == data
    
    def test_get_prev(self):
        assert self.sls.get_prev() == None
    
    def test_set_prev(self):
        new_node = recursive_indexer.sll("other data")
        self.sls.set_prev(new_node)
        assert self.sls.get_prev() == new_node

if __name__ == "__main__":
    pytest.main()
