T = [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10.];
D = [486.   481.14 466.56 442.26 408.24 364.5  311.04 247.86 174.96  92.34 0.  ];

% we want to see if this experiment obeys the laws of physics, i.e. whether
% or not the ball falls with respect to gravity. Therefore we should
% approximate the data with a parabolic shape
scatter(T, D);
[coeff] = func_fit(T, D, "approximate", "poly", 2);

hold on;
x = linspace(min(T), max(T), 1100);
y = polyval(coeff, x);
% plot line
plot(x, y);
hold off;

% calculate errors
residual = [];
absolute = [];
for yi = 1:size(D, 2)
    r = D(yi) - y(yi*100);
    a = D(yi) / y(yi*100);
    residual = [residual r];
    absolute = [absolute a];
end
% print out errors
residual
absolute

% to show the laws of gravity are obeyed calculate acelleration
timeDiff = x(size(x, 2)) - x(size(x, 2)-1);
distDiff = y(size(y, 2)) - y(size(y, 2)-1);
velFinal = distDiff./timeDiff;
timeDiff = x(2) - x(1);
distDiff = y(2) - y(1);
velInitial = distDiff./timeDiff;

accell = (velFinal-velInitial)/x(end)

% After running this script the accell value calculated should be -9.7112
% which is close to the actual 9.81. The small inaccuracy leftover may be
% due to some enviromental/experimental errors when doing the actual
% experiment/collecting data.