
import dal
from models import *

def insert_item(item: Item):
    dal.insert_item(item)

def get_items():
    return dal.get_items()

def delete_item(item_id: int):
    return dal.delete_item(item_id)
