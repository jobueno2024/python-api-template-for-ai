# プロンプト1
次の仕様でディレクトリ構成を作成して

### 仕様
```markdown
- Python
- API by FastAPI
- Onion architecture
- Docker + devcontainer
```


# プロンプト2
次の仕様でディレクトリ構成を作成して
### 仕様
- Python
- API by FastAPI
- Onion architecture
- Docker + devcontainer

#### 使用ディレクトリ
- domain
- infrastructure
- presentation
- usecase

# レスポンス2
my_project/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── app/
│   ├── domain/
│   │   ├── __init__.py
│   │   └── entities.py  # Domain entities
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   └── repositories.py # Data access layer (repositories)
│   ├── presentation/
│   │   ├── __init__.py
│   │   └── api.py # API endpoints (controllers)
│   ├── usecase/
│   │   ├── __init__.py
│   │   ├── use_cases.py # Business logic (use cases/interactors)
│   │   └── exceptions.py # Custom exceptions for use cases
│   ├── __init__.py
│   └── schemas.py  # Data transfer objects (DTOs/schemas)
├── main.py        # Entry point for the FastAPI application
├── requirements.txt
└── docker-compose.yml


# プロンプト3
上記のディレクトリ構成のソースコードを生成するshell scriptを作成して。

# レスポンス3
```bash
#!/bin/bash

# Create project directory and navigate into it
mkdir my_fastapi_project && cd my_fastapi_project

# Create app directory structure
mkdir -p app/{domain,infrastructure,presentation,usecase}

# Create __init__.py files
touch app/__init__.py
touch app/domain/__init__.py
touch app/infrastructure/__init__.py
touch app/presentation/__init__.py
touch app/usecase/__init__.py

# Create and populate Python files (using cat << EOF)

cat << EOF > app/domain/entities.py
class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
EOF

cat << EOF > app/usecase/use_cases.py
from domain.entities import Item
from usecase.interactors import ItemInteractor  # Updated import path

class CreateItemUseCase:
    def __init__(self, item_interactor: ItemInteractor):
        self.item_interactor = item_interactor

    def execute(self, name: str, description: str) -> Item:
        return self.item_interactor.create_item(name, description)
EOF


cat << EOF > app/usecase/interactors.py
from domain.entities import Item
from infrastructure.repositories import ItemRepository


class ItemInteractor:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def create_item(self, name: str, description: str) -> Item:
        item = Item(name, description)
        self.item_repository.save(item)
        return item

EOF

cat << EOF > app/infrastructure/repositories.py
from domain.entities import Item


class ItemRepository:
    def save(self, item: Item):
        print(f"Saving item: {item.name} - {item.description}")
EOF

cat << EOF > app/presentation/api.py
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
EOF

cat << EOF > app/schemas.py
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str
EOF

cat << EOF > main.py
from fastapi import FastAPI

from presentation.api import router


app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
EOF


# Create requirements.txt
cat << EOF > requirements.txt
fastapi
uvicorn
pydantic
EOF

# Create Dockerfile
cat << EOF > .devcontainer/Dockerfile
FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
EOF


cat << EOF > .devcontainer/devcontainer.json
{
    "name": "Python 3.11",
    "image": "mcr.microsoft.com/devcontainers/python:0-3.11",
    "features": {
        "ghcr.io/devcontainers/features/node:1": {},
        "ghcr.io/devcontainers-contrib/features/terraform:1": {}
    },

    // Use 'forwardPorts' to make any exposed ports available locally.
    "forwardPorts": [8000],

    // Use 'postCreateCommand' to run commands after the container is created.
    "postCreateCommand": "pip3 install --upgrade pip && pip3 install -r requirements.txt",

    // Configure tool-specific properties.
    "customizations": {
        // Configure properties specific to VS Code.
        "vscode": {
            // Set *default* container specific settings.json values on container create.
            "settings": {
                "python.defaultInterpreterPath": "/usr/local/bin/python",
                "python.linting.enabled": true,
                "python.linting.pylintEnabled": true,
                "python.formatting.autopep8Path": "/usr/local/py-utils/bin/autopep8",
                "python.formatting.blackPath": "/usr/local/py-utils/bin/black",
                "python.formatting.yapfPath": "/usr/local/py-utils/bin/yapf",
                "python.linting.pylintPath": "/usr/local/py-utils/bin/pylint",
                "python.linting.flake8Path": "/usr/local/py-utils/bin/flake8"
            },
             "extensions": [
                "ms-python.python",
                "ms-python.vscode-pylance"
            ]
        }
    },

    // Uncomment to connect as root instead. More info: https://aka.ms/dev-containers-non-root.
    "remoteUser": "vscode"
}
EOF





# Create docker-compose.yml
cat << EOF > docker-compose.yml
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
EOF

chmod +x generate_project.sh

echo "Project created. Run './generate_project.sh' to generate files."
```



# プロンプト4
Dockerfileにポート8000を追加して

ports:
  - "8000:8000"

# プロンプト5

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
のmain:appを/app/main.pyから実行するように変更して