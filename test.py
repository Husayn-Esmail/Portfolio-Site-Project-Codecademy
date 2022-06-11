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
    

def read_images(path: str, prev_path: str = None):
    # if first_run and os.path.isdir(path):
    #     parent_dirs = os.listdir(path)
    #     for dir in parent_dirs:
    #         paths.append({dir: []})
    #     first_run = False
    # FIXME: Still need to tailor output to something desirable
    if os.path.isdir(path):
        listed = os.listdir(path)
        for item in listed:
            new_path = path + '/' + item
            paths.append({new_path:[]})
            read_images(new_path, path)
    else:
        for item in paths:
            if prev_path in item:
                item[prev_path].append(path)


read_images(path)


for path in paths:
    print(path)