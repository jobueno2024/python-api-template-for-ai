# python-api-template-for-ai
Default template + business logic by ai

1. Python
2. API by FastAPI
3. Onion architecture
4. Docker + devcontainer
5. AWS or Google Cloud

# Run container
cd my_fastapi_project/app
docker compose up -d

# Request
curl -X POST -H "Content-Type: application/json" -d '{"name": "My Item", "description": "A test item"}' http://localhost:8000/items/

# Shutdown container
docker compose down

