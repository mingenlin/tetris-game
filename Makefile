PHONY: venv dep

venv:
	python3 -m venv .venv	

dep:
	@echo "Downloading dependencies..."
	@pip install -r requirements.txt