% Vectorize the following
% Note the use of the tic/toc calls to time execution
% Compare the time once you have vectorized it

tic
for i = 1:1000
    t(i) = 2*i;
    y(i) = sin (t(i));
end
toc

tLoop = toc;

tic
i2 = 1:1000;
t2 = 2*i;
y2 = sin(t2);
toc

tVector = toc;

fprintf("Difference is %f seconds.\n", tLoop - tVector);

clear;
