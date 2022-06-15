import pytest
from recursive import recursive_indexer
import jsonpickle

import recursive
class TestProject:
    def setup(self):
        self.name = "test"
        self.images = []
        self.project = recursive_indexer.Project(self.name, self.images)

    def test_get_name(self):
        assert self.project.get_name() == self.name

    def test_set_name(self):
        new_name = "new name"
        self.project.set_name(new_name)
        assert self.project.get_name() == new_name

    def test_get_images(self):
        assert self.project.get_images() == self.images
    
    def test_set_images(self):
        new_images = ['image1.jpg', 'image2.jpg']
        self.project.set_images(new_images)
        assert self.project.get_images() == new_images
    
    def test_add_image(self):
        new_image = "test.jpg"
        self.project.add_image(new_image)
        assert new_image in self.project.get_images()

    def test_get_description(self):
        assert self.project.get_description() == ""
    
    def test_set_description(self):
        desc = "test"
        self.project.set_description(desc)
        assert self.project.get_description() == desc
    
    def test_get_json_returns_value(self):
        assert self.project.to_json() is not None

    def test_type_get_json(self):
        expected = str
        actual = type(self.project.to_json())
        assert actual == expected

    def test_get_json_is_object(self):
        expected = recursive_indexer.Project
        actual = type(jsonpickle.decode(self.project.to_json()))
        assert actual == expected
    
    def test_get_json_retains_data(self):
        expected = self.project.__dict__
        actual = jsonpickle.decode(self.project.to_json()).__dict__
        assert actual == expected

if __name__ == '__main__':
    pytest.main()