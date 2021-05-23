.PHONY: install
install:
	@cd deployment && bash install.sh

.PHONY: run
run:
	@. env/bin/activate && cd src && python app.py
