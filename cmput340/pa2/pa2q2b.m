scatter(x, y);
% a quadratic function seems to fit this data the best
[coeff] = func_fit(x, y, "approximate", "poly", 2);
hold on;
x1 = linspace(min(x), max(x), 1000);
y1 = polyval(coeff, x1);
% plot line
plot(x1, y1);
ylim([-5, 30]);
hold off;

% the coefficients given by my func_fit function are -0.133012950107605,
% 0.00669861081385174, 1.01137095034711 Since I am using a monomial basis
% of degree 2, my interpolation equation would be:
% pn-1(t) = 1.01137095034711t^2 + 0.00669861081385174*t - 0.133012950107605
% the derivative of this equation is:
% p'(t) = 2.02274190069*t + 0.00669861081385174
% the area under the curve, or the integral of the function from -5 to 5, 
% of the curve is equal to 82.95078302784978