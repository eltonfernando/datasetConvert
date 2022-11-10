from .repository import AnotationRepo

repo = AnotationRepo()
repo.inset()
data = repo.select()
print(data)