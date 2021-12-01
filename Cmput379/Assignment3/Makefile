CFLAGS=-I -W -O.

all: server client

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

clean:
	rm *.o server client
