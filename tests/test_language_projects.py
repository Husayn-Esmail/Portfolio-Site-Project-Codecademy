import pytest
from recursive import recursive_indexer

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


if __name__ == '__main__':
    pytest.main()