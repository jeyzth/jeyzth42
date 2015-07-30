#PROJECT="/home/jeyzth/tg2env/jeyzth42"
PROJECT="./"
env:
	./start.env 
test:  
	cd $(PROJECT) && ./run.gearbox && nosetests
run:
	cd $(PROJECT) && ./run.gearbox
stop:
	cd $(PROJECT) && gearbox serve --stop-daemon
	
