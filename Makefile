
all:
	python viz.py
	cp output/* ~/workspace/jcaip.github.io/images/R/

clean:
	rm output/*
