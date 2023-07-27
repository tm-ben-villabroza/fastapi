api: venv/bin/activate
	./venv/bin/uvicorn main:app --reload

rebuild-venv: requirements.txt
	rm -rf venv
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

postgres: docker-compose.yaml
	sudo docker compose up
