from fastapi import APIRouter, Depends

from domain.entities import Item
from usecase.use_cases import CreateItemUseCase
from usecase.interactors import ItemInteractor
from infrastructure.repositories import ItemRepository
from schemas import ItemCreate

router = APIRouter()


class ItemController:
    def __init__(self, create_item_use_case: CreateItemUseCase):
        self.create_item_use_case = create_item_use_case

    @router.post("/items/", response_model=ItemCreate)
    async def create_item(item: ItemCreate):  # Remove query parameter designation
        created_item = create_item_use_case.execute(item.name, item.description)
        return ItemCreate(name=created_item.name, description=created_item.description)


item_repository = ItemRepository()
item_interactor = ItemInteractor(item_repository)
create_item_use_case = CreateItemUseCase(item_interactor)
item_controller = ItemController(create_item_use_case)
