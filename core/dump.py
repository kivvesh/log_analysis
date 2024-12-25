import json
import os.path
from textwrap import indent

from settings import ROOT_DIR

def dump_allure(data):
    with open(os.path.join(ROOT_DIR, 'allure.json'), 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=3)
