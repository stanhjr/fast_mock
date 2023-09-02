from repositories.abstract import AbstractRepository
from schemas.item import ItemSchema


class ItemService:
    def __init__(self, tasks_repo: AbstractRepository):
        self.item_repo: AbstractRepository = tasks_repo()

    async def add_item(self, task: ItemSchema):
        tasks_dict = task.model_dump()
        task_id = await self.item_repo.add_one(tasks_dict)
        return task_id

    async def get_items(self):
        tasks = await self.item_repo.find_all()
        return tasks
