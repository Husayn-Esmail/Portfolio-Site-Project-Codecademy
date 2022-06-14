from timeit import timeit
# statement = """"""
import os
from memory_profiler import profile


class Project:
    def __init__(self, name, images):
        self.__name = name
        self.__images = images
        self.__description = ""

    def set_name(self, new_name):
        self.__name = new_name

    def add_image(self, image: str):
        self.__images.append(image)
    
    def set_images(self, new_list):
        self.__images = new_list
    
    def get_images(self):
        return self.__images
    
    def set_description(self, description):
        self.__description = description
    
    def get_description(self):
        return self.__description
    
    def get_name(self):
        return self.__name
    
    def __str__(self):
        return """
        name: %s
        images: %s
        description: %s
        """ % (self.get_name(), str(self.get_images()), self.get_description())

class LanguageProjects:
    def __init__(self, prog_language):
        self.__prog_language = prog_language
        self.__projects = []
    
    def get_prog_language(self):
        return self.__prog_language
    
    def get_projects(self):
        return self.__projects
    
    def add_project(self, project: Project):
        self.__projects.append(project)

    def set_projects(self, projects):
        self.__projects = projects

    def set_prog_language(self, prog_language):
        self.__prog_language = prog_language
    
    def __str__(self):
        return """
        prog_language = %s
        projects = %s
        """ % (self.get_prog_language(), str(self.get_projects()))
    
class sllnode:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
    
    def get_data(self):
        return self.__data
    
    def get_prev(self):
        return self.__prev
    
    def set_data(self, new_data):
        self.__data = new_data
    
    def set_prev(self, node):
        self.__prev = node


# @profile
def read_images(projects: list, path: str, project: LanguageProjects = None,
                prev_path: str = None, prev_item: sllnode = None):
    # FIXME: Still need to tailor output to something desirable
    is_dir = os.path.isdir(path)
    if is_dir:
        listed = os.listdir(path)
        for item in listed:
            new_lang = LanguageProjects(item)
            new_path = path + '/' + item
            if prev_item is None:
                new_item = sllnode(item)
                read_images(projects, new_path, new_lang, path, new_item)
                projects.append(new_lang)
            else:
                new_item = sllnode(item)
                new_item.set_prev(prev_item)
                read_images(projects, new_path, new_lang, path, new_item)

    else:
        items = os.listdir(prev_path)
        # print(prev_item.get_prev().get_data())
        # while loop iterating back to prev = none to figure out parent directory
        temp = prev_item
        while temp.get_prev() != None:
            temp = temp.get_prev()
        image_dir = temp.get_data()
        new_project = Project(image_dir, items)
        for item in projects:
            if item.get_prog_language() == temp:
                item.add_project(new_project)
        # print(new_project.__dict__)
        # print(prev_item.get_data())
        # for item in projects:
        #     print(item.__dict__)


if __name__ == "__main__":
    path = 'portfolio-site/static/img'
    projects = []
    read_images(projects, path)
    for item in projects:
        print(item)
    # print(timeit(stmt = statement, number = 5000))
