function [pos, J] = evalRobot2D(l, theta)
l1 = l(1);
l2 = l(2);
theta1 = theta(1);
theta2 = theta(2);
x = l1*cos(theta1)+l2*cos(theta1+theta2);
y = l1*sin(theta1)+l2*sin(theta1+theta2);

pos = [x y];
q1 = -l2*sin(theta1+theta2)-l1*sin(theta1);
q2 = -l2*sin(theta1+theta2);
q3 = l2*cos(theta1+theta2)+l1*cos(theta1);
q4 = l2*cos(theta1+theta2);
J = [q1 q2; q3 q4];