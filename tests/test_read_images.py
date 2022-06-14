from recursive import recursive_indexer
import pytest
import os

class TestRecursiveIndexer:
    def setup(self):
        self.path = 'portfolio-site/static/img'
        self.projects = []
        recursive_indexer.read_images(self.projects, self.path)
    
    def test_projects_not_empty(self):
        assert self.projects != []
    
    def test_no_favicons(self):
        for item in self.projects:
            assert item.get_prog_language() != "favicons"
    
    def test_projects_length(self):
        expected = os.listdir(self.path)
        # minus one to omit favicons
        assert len(self.projects) == (len(expected) - 1) 

    def test_projects_are_parent_dir(self):
        expected = os.listdir(self.path)
        for item in self.projects:
            assert item.get_prog_language() in expected
    
    def test_project_in_projects_has_value(self):
        pass

    def test_project_values_correct(self):
        pass
    
