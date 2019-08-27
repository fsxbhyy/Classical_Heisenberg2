src=$(wildcard *.cpp)
obj=$(src:.cpp=.o)
CXX=g++
CXXFLAGS=-std=c++11
main:$(obj)
	$(CXX) $(obj) -o main

.PHONY: clean
clean:
	rm -f $(obj) main
