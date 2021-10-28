README FOR ASSIGNMENT 2
STUDENT: echiu

INCLUDED FILES:

main.c: the main function houses the producer as well as the start up routine.
After taking the command line arguments a file is opened and threads are created.
The threads are then created and the producer loops and takes in tasks until a EOF
is recieved.

functions.c: this file houses code for the threads and other functions I have used
for the program. Notable functions are the createThreads(), closeThreads(), threadsStart()
functions, which open the threads, call pthread_joint() to wait on the threads respectively.
The third function is the routine that createThreads call, which infinetley loop and take jobs
from the queue until a global variable notifies the threads that the EOF has been sent.

ASSUMPTIONS:

The assumptions done for this assignment are the sizes of the input. I since the possible
size of n for the T commands were not given, I assumed it would be the same as S commands,
that is 0 < n < 100, and have allocated memory equal to that asusmption. The id for the log
is given a buffer of 100 characters, which is probably too big but I decided it was better
safe than sorry.

I understand that I may have also overused global variables in my assignment. I understand
you can pass in structs to a thread when creating it but for my solution I had different
groups of variables and it did not make sense to me to pass some in as structs then still
have others ben global variables, so I decided to make them all be global variables and was
careful to make sure that they would not affect the program.

APPROACH:

I treated the main function as the main function as the producer and opened up n threads to
be consumers. This made sense to me as opposed to opening another thread as the producer and
having main just waiting for everything else to happen. I used POSIX semaphores to access the
queue and other variables that the thread had to edit, such as summary numbers and the start
time of the program for the sake of printing out the timestamps.

HOW TO COMPILE AND RUN:

I have changed the makefile to have -O and removed the -g tag so just calling make should make
the program as per the specifications. To run call ./prodcon as well as the # of threads to run
and the optional 3 that the log file should be labelled as.