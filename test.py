import os

path = 'portfolio-site/static/img'
paths = []

def read_images(path: str, prev_path: str = None):
    # if first_run and os.path.isdir(path):
    #     parent_dirs = os.listdir(path)
    #     for dir in parent_dirs:
    #         paths.append({dir: []})
    #     first_run = False
    
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