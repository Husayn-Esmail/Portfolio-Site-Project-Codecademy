from timeit import timeit
# statement = ''''''
import os
from memory_profiler import profile


class Project:
    '''
    Represents a project results structure.
    '''
    def __init__(self, name: str, images: list):
        '''
        Requires a name and a list of image names upon instantiation, can have
        a description added to the project later.
        '''
        self.__name = name
        self.__images = images
        self.__description = ""

    def set_name(self, new_name: str):
        '''sets name of project, requires new_name'''
        self.__name = new_name
        return None

    def add_image(self, image: str):
        '''Used to add an image to list of images, requires an image name.'''
        self.__images.append(image)
        return None

    def set_images(self, new_list: list):
        '''Used to set the entire list of images. Requires a list of images.'''
        self.__images = new_list
        return None
    
    def get_images(self):
        '''Returns the project list of images. '''
        return self.__images
    
    def set_description(self, description: str):
        '''
        Used to set the project description. Requires one argument description
        '''
        self.__description = description
        return None

    def get_description(self):
        '''Returns the project description.'''
        return self.__description
    
    def get_name(self):
        '''Returns the project name'''
        return self.__name
    
    def __str__(self):
        '''Produces a string version of the project.'''
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
def read_images(projects: list, path: str,
                prev_path: str = None, prev_item: sllnode = None):
    is_dir = os.path.isdir(path)
    if is_dir:
        dir_contents = os.listdir(path)
        for file_name in dir_contents:
            if file_name == "favicons": continue # excludes favicons
            new_lang = LanguageProjects(file_name)
            new_path = path + '/' + file_name
            if prev_item is None:
                new_item = sllnode(file_name)
                projects.append(new_lang)
                read_images(projects, new_path, prev_path=path, prev_item=new_item)
            else:
                new_item = sllnode(file_name)
                new_item.set_prev(prev_item)
                read_images(projects, new_path, prev_path=path, prev_item=new_item)
    else:
        items = os.listdir(prev_path)
        lang = prev_item
        while lang.get_prev() != None:
            lang = lang.get_prev()
        lang = lang.get_data()
        name = prev_item.get_prev().get_data()
        new_project = Project(name, items)
        for technology in projects:
            if technology.get_prog_language() == lang:
                exist = False
                for project in technology.get_projects():
                    if project.get_name() == new_project.get_name():
                        exist = True
                if not exist:
                    technology.add_project(new_project)


if __name__ == "__main__":
    path = 'portfolio-site/static/img'
    projects = []
    read_images(projects, path)
    for item in projects:
        print(item)
        for project in item.get_projects():
            print(project)

# print(timeit(stmt = statement, number = 5000))
