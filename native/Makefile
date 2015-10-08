CXX?=c++
LD=$(CXX)

PROJECT=jl-pick

VPATH=src

CFLAGS?=-O2

build: $(PROJECT)

$(PROJECT): main.o
	$(LD) -lc $(LDFLAGS) main.o -o "bin/$(PROJECT)"

main.o:
	$(CXX) -c -g -Winline -Wall -Wconversion -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 $(CFLAGS) src/main.cpp

clean:
	rm -f *.o "bin/$(PROJECT)"

install: build
	install "bin/$(PROJECT)" "$(PREFIX)/bin"

test:
	sh tests/all.sh
