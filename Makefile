PROJECT="/home/jeyzth/tg2env/jeyzth42"


test:  
	cd $(PROJECT) && ./start.env && ./run.gearbox && nosetests
run:
	cd $(PROJECT) && ./start.env && ./run.gearbox
stop:
	cd $(PROJECT) && gearbox serve --stop-daemon
	
