NAME=gelnarbot

all: build_and_run
	
build_and_run:
	make build
	make run

build:
	sudo docker-compose build

run:
	sudo docker-compose up

console:
	sudo docker-compose run $(NAME) gelnarBot_console

build_and_console:
	make build
	make console

# The following are non-docker options

nd_run:
	python gelnar_bot/gelnar_bot.py

nd_console:
	python -c "from gelnar_bot.gelnar_bot import noun_test_console as f; f()"
