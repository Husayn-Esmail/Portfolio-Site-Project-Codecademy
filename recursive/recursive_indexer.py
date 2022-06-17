# from timeit import timeit
# statement = ''''''
import os
from memory_profiler import profile
import jsonpickle

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

    
    def get_images(self):
        '''Returns the project list of images. '''
        return self.__images
    
    def get_description(self):
        '''Returns the project description.'''
        return self.__description
    
    def get_name(self):
        '''Returns the project name'''
        return self.__name

    def set_name(self, new_name: str):
        '''sets name of project, requires new_name'''
        self.__name = new_name
        return None

    def set_images(self, new_list: list):
        '''
        Used to set the entire list of images. Requires a list of images.
        '''
        self.__images = new_list
        return None

    def set_description(self, description: str):
        '''
        Used to set the project description. Requires one argument description
        '''
        self.__description = description
        return None
    
    def add_image(self, image: str):
        '''
        Used to add an image to list of images, requires an image name.
        '''
        self.__images.append(image)
        return None

    def to_json(self):
        '''
        Converts Project object to json format so it can be used 
        by javascript.
        '''
        return jsonpickle.encode(self)
    
    def __str__(self):
        '''Produces a string version of the project.'''
        return """
        name: %s
        images: %s
        description: %s
        """ % (self.get_name(), 
                str(self.get_images()), 
                self.get_description())

class ProjectsTechnology:
    '''
    Represents a compilation of projects for a specific programming language.
    '''
    def __init__(self, prog_language: str):
        '''
        Upon instantiation, only requires the programming language to be
        specified. Projects can be updated later.
        '''
        self.__prog_language = prog_language
        self.__projects: Project = []
    
    def get_prog_language(self):
        '''
        Returns programming language name.
        '''
        return self.__prog_language
    
    def get_projects(self):
        '''
        Returns list of project objects.
        '''
        return self.__projects
    
    def add_project(self, project: Project):
        '''
        Allows functionality to add projects to project list. Requires a
        new project.
        '''
        self.__projects.append(project)
        return None

    def set_projects(self, projects: list):
        '''
        Allows to set an entire list of projects all at once (overriding
        whatever is currently in self.__projects). Requires one argument,
        a list of projects.
        '''
        self.__projects = projects
        return None

    def set_prog_language(self, prog_language: str):
        '''
        Allows functionality to update the programming language. Requires one
        argument, the prog_language.
        '''
        self.__prog_language = prog_language
        return None
    
    def to_json(self):
        '''
        Converts Project object to json format so it can be used 
        by javascript.
        '''
        return jsonpickle.encode(self)
    
    def __str__(self):
        '''String representation of the object'''
        return """
        prog_language = %s
        projects = %s
        """ % (self.get_prog_language(), str(self.get_projects()))
    
class sllnode:
    '''
    Represents a node of a singly linked list. This node works in reverse
    compared to a normal node. It holds data and a previous rather than
    a next.
    '''
    def __init__(self, data):
        '''
        Must be initialized with a single argument, data which can be of any
        type.
        '''
        self.__data = data
        self.__prev = None
    
    def get_data(self):
        """
        Returns the node's data.
        """
        return self.__data
    
    def get_prev(self):
        """
        Returns the node's previous node.
        """
        return self.__prev
    
    def set_data(self, new_data):
        '''
        Used to set the data value of a node. Requires new data of any type.
        '''
        self.__data = new_data
        return None

    def set_prev(self, node: 'sllnode'):
        '''
        Used to set the previous node of a node. Requires another node.
        '''
        self.__prev = node

# @profile
def index_images(projects: list, 
                path: str,
                ignored: list,
                prev_path: str = None, 
                prev_item: sllnode = None):
    """
    Recursively traverses a path to determine it's contents. It populates
    a list which is passed in (projects). Requires the projects list and path.
    prev_path and prev_item default as None and are updated as the function is
    recursively called. As it comes out, it builds the list of objects
    using Project, sllnode and LanguageProjects.
    """
    is_dir = os.path.isdir(path)
    if is_dir:
        dir_contents = os.listdir(path)
        for file_name in dir_contents:
            if file_name in ignored: continue # excludes favicons
            new_lang = ProjectsTechnology(file_name)
            new_path = path + '/' + file_name
            if prev_item is None:
                new_item = sllnode(file_name)
                projects.append(new_lang)
                index_images(projects, 
                            new_path,
                            ignored, 
                            prev_path=path, 
                            prev_item=new_item)
            else:
                new_item = sllnode(file_name)
                new_item.set_prev(prev_item)
                index_images(projects, 
                new_path,
                ignored,
                prev_path=path, 
                prev_item=new_item)
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

def get_descriptions(path: str, projects: list):
    '''
    Because opening and reading files will likely be a slow operation, I want
    to do it as few times as possible. iterate through projects, get and
    populate their descriptions based on project name. Ideally I would like to
    make the description capturing and indexing happen at the same time...
    eventually... 
    '''
    for project in projects:
        project_name = project.get_name()
        desc_file_name = project_name + '.txt'
        full_path = path + '/' + desc_file_name
        try:
            with open(full_path, "r") as f:
                content = f.read()
                project.set_description(content)
        except Exception as exc:
            print(exc)


def get_projects_for_display(image_path: str, desc_path: str, ignored: list):
    '''
    requires path to images and path to descriptions.
    calls helper functions to fully build out each ProjectsTechnology object
    and returns a list of completely populated objects.
    '''
    technologies = []
    index_images(technologies, image_path, ignored)
    for tech in technologies:
        tech_projects = tech.get_projects()
        get_descriptions(desc_path, tech_projects)
    
    return technologies


if __name__ == "__main__":
    path = 'portfolio-site/static/img'
    path_for_desc = 'portfolio-site/static/descriptions'
    new_list = get_projects_for_display(path, path_for_desc, [])
    for ls in new_list:
        print(ls.get_projects()[0].get_description())
    # x = projects[0].get_projects()[0].to_json()
    # print(x)
    # print(type(x))
    # x_decode = jsonpickle.decode(x)
    # print(type(x_decode))
    # for item in projects:
    #     print(item)
    #     for project in item.get_projects():
    #         print(project)

# print(timeit(stmt = statement, number = 5000))
