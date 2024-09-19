.PHONY: run build stop

# Run the FastAPI app in detached mode using Docker Compose
run:
	docker-compose up --build

# Stop and remove the running containers
stop:
	docker-compose down

# Clean: Remove all containers and images
clean:
	docker-compose down -v --remove-orphans
	docker system prune -af --volumes

install.local:
	pip install -r requirements.txt
