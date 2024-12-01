from fastapi import APIRouter

from domain.entities import Item
from usecase.use_cases import CreateItemUseCase
from usecase.interactors import ItemInteractor
from infrastructure.repositories import ItemRepository
from schemas import ItemCreate

router = APIRouter()

item_repository = ItemRepository()
item_interactor = ItemInteractor(item_repository)
create_item_use_case = CreateItemUseCase(item_interactor)



@router.post("/items/", response_model=ItemCreate)
def create_item(item: ItemCreate) -> ItemCreate:
    created_item = create_item_use_case.execute(item.name, item.description)
    return ItemCreate(name=created_item.name, description=created_item.description)
