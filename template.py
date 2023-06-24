import os


dir = [
    os.path.join('Data', 'Raw'),
    os.path.join('Data', 'Processed'),
    'Notebook',
    'Saved_Model',
    "logger",
    'src'
]

for dir_ in dir:
    os.makedirs(dir_, exist_ok =True)
    with open(os.path.join(dir_, ".gitkeep"), 'w') as f:
        pass

file = [
    os.path.join('src', '__init__.py'),
    os.path.join('logger', '__init__.py')
]

for file_ in file:
    with open(file_, "w") as f:
        pass
    