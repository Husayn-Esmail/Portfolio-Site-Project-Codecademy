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
    is_dir = os.path.isdir(path)
    if is_dir:
        listed = os.listdir(path)
        for item in listed:
            project = LanguageProjects(item)
            new_path = path + '/' + item
            # paths.append({new_path:[]})
            print("item: ", item)
            read_images(projects, new_path, project, path, item)
            if project.get_projects() != []:
                projects.append(project)
    else:
        # builds project object
        items = os.listdir(prev_path)
        new_project = Project(prev_item, items)
        print(prev_item)
        # print(new_project.__dict__)
        for item in projects:
            print(item.__dict__)

if __name__ == "__main__":
    projects = []
    read_images(projects, path)


for path in paths:
    print(path)