build:
	clang++-18 -std=c++23 main.cpp -o main
	./main

run:
	clang++-18 -std=c++23 main.cpp -o main
	./main
	rm -rf main

clean: main
	rm -rf main