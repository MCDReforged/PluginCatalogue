import os

here = os.path.dirname(__file__)
root = os.path.abspath(os.path.join(here, '..'))

TEMPLATE = os.path.join(here, 'templates')
PLUGINS_FOLDER = os.path.join(root, 'plugins')
LABEL_FILE = os.path.join(PLUGINS_FOLDER, 'labels.json')
GENERATED_DOC_FOLDER = os.path.join(root, 'generated')


