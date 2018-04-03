album.png: album.py
	python album.py 
album.py: album.txt
album.txt: album.cpp
	c++ album.cpp -o album 
	./album > album.txt

