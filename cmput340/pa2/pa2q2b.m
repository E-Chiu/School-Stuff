scatter(x, y);
[coeff] = func_fit(x, y, "approximate", "poly", 2);

hold on;
x1 = linspace(min(x), max(x), 1000);
y1 = polyval(coeff, x1);
% plot line
plot(x1, y1);
ylim([-5, 30]);
hold off;