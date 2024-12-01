from domain.entities import Item
from usecase.interactors import ItemInteractor  # Updated import path

class CreateItemUseCase:
    def __init__(self, item_interactor: ItemInteractor):
        self.item_interactor = item_interactor

    def execute(self, name: str, description: str) -> Item:
        return self.item_interactor.create_item(name, description)
