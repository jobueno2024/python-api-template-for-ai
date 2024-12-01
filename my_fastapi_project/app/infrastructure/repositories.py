from domain.entities import Item


class ItemRepository:
    def save(self, item: Item):
        print(f"Saving item: {item.name} - {item.description}")
