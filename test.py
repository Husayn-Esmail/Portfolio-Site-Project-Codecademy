import os

path = 'portfolio-site/static/img'
paths = []

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
    
class sll:
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
        self.__prv = node
    

def read_images(projects, path: str, project: LanguageProjects = None,
                prev_path: str = None, prev_item: sll = None):
    # if first_run and os.path.isdir(path):
    #     parent_dirs = os.listdir(path)
    #     for dir in parent_dirs:
    #         paths.append({dir: []})
    #     first_run = False
    # FIXME: Still need to tailor output to something desirable
    if os.path.isdir(path):
        listed = os.listdir(path)
        for item in listed:
            new_lang = LanguageProjects(item)
            new_path = path + '/' + item
            if prev_item == None:
                new_item = sll(item)
                read_images(projects, new_path, new_lang, path, new_item)
            else:
            # paths.append({new_path:[]})
                new_item = sll(item)
                new_item.set_prev(prev_item)
                read_images(projects, new_path, new_lang, path, new_item)
            if new_lang.get_projects() != []:
                projects.append(new_lang)
    else:
        for item in paths:
            if prev_path in item:
                item[prev_path].append(path)

if __name__ == "__main__":
    projects = []
    read_images(projects, path)


for path in paths:
    print(path)