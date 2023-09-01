from schemas.brands import BrandSchemaAdd
from utils.repository import AbstractRepository


class CategoryService:
    def __init__(self, tasks_repo: AbstractRepository):
        self.tasks_repo: AbstractRepository = tasks_repo()

    async def add_category(self, task: BrandSchemaAdd):
        tasks_dict = task.model_dump()
        task_id = await self.tasks_repo.add_one(tasks_dict)
        return task_id

    async def get_categories(self):
        tasks = await self.tasks_repo.find_all()
        return tasks
