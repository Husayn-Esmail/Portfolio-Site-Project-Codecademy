import pytest
from recursive import recursive_indexer
import jsonpickle
class TestLanguageProjects:
    def setup(self):
        self.prog_lang = "test"
        self.project = recursive_indexer.LanguageProjects(self.prog_lang)
    
    def test_get_prog_language(self):
        assert self.project.get_prog_language() == self.prog_lang
    
    def test_set_prog_language(self):
        new_lang = "new lang"
        self.project.set_prog_language(new_lang)
        assert self.project.get_prog_language() == new_lang

    def test_get_projects(self):
        assert self.project.get_projects() == []
    
    def test_add_project(self):
        new_project = recursive_indexer.Project("test", [])
        self.project.add_project(new_project)
        assert new_project in self.project.get_projects()
    
    def test_set_projects(self):
        projects = ["item"]
        self.project.set_projects(projects)
        assert self.project.get_projects() == projects
    
    def test_get_json_returns_value(self):
        assert self.project.to_json() is not None

    def test_type_get_json(self):
        expected = str
        actual = type(self.project.to_json())
        assert actual == expected

    def test_get_json_is_object(self):
        expected = recursive_indexer.LanguageProjects
        actual = type(jsonpickle.decode(self.project.to_json()))
        assert actual == expected
    
    def test_get_json_retains_data(self):
        expected = self.project.__dict__
        actual = jsonpickle.decode(self.project.to_json()).__dict__
        assert actual == expected


if __name__ == '__main__':
    pytest.main()