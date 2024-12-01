from domain.entities import Item
from infrastructure.repositories import ItemRepository


class ItemInteractor:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def create_item(self, name: str, description: str) -> Item:
        item = Item(name, description)
        self.item_repository.save(item)
        return item

