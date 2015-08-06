
all: build_and_run
	
build_and_run:
	make build
	make run

build:
	sudo docker-compose build

run:
	sudo docker-compose up
