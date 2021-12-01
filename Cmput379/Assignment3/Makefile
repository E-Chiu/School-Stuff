CFLAGS=-I -W -O.

all: server client manuals

server: tands.o functions.o server.o
	gcc -o server server.o tands.o functions.o

client: tands.o functions.o client.o
	gcc -o client client.o tands.o functions.o
	
server.o: server.c
	gcc -c server.c

client.o: client.c
	gcc -c client.c

tands.o: tands.c
	gcc -c tands.c

functions.o: functions.c
	gcc -c functions.c

manuals: client.1 server.1
	groff -Tpdf -man client.1 > client.pdf
	groff -Tpdf -man server.1 > server.pdf

clean:
	rm *.o *.pdf server client
