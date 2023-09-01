from schemas.item_schema import ItemSchema
from utils.repository import AbstractRepository


class ItemService:
    def __init__(self, tasks_repo: AbstractRepository):
        self.tasks_repo: AbstractRepository = tasks_repo()

    async def add_task(self, task: ItemSchema):
        tasks_dict = task.model_dump()
        task_id = await self.tasks_repo.add_one(tasks_dict)
        return task_id

    async def get_tasks(self):
        tasks = await self.tasks_repo.find_all()
        return tasks
