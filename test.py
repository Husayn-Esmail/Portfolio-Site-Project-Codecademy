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
    

    

def read_images(projects, path: str, project: LanguageProjects = None,
                prev_path: str = None, prev_item: str = None):
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
            # paths.append({new_path:[]})
            read_images(new_path, new_lang, path)
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