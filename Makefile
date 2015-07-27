PROJECT="/home/jeyzth/tg2env/jeyzth42"


test:  
	cd $(PROJECT) && nosetests
run:
	cd $(PROJECT) && gearbox serve 

