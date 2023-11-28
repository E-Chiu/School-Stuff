function J = fdJacob2D(l, theta, h)
col1 = ( evalRobot2D(l, theta+[h;0]) - evalRobot2D(l, theta-[h;0]) ) / (2*h);
col2 = ( evalRobot2D(l, theta+[0;h]) - evalRobot2D(l, theta-[0;h]) ) / (2*h);
J = [col1' col2'];

% a some of the results are close enough to be useful, at h=1 and h=7
% it may be better to use the approximation when the equation itself is too
% expensive to calculate