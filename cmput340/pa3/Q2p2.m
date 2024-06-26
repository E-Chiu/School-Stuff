% a)
l = [.8,.7];
n = 1000;
theta0 = [pi,pi,pi];
theta = [pi/3, pi/4, pi/3]; %position here is 0.1094    0.1895    1.3690
desired = [0, 0, 1];
oppQuad = [-1.5, -1.5, -1.5]; %opposite quadrant is - - -
mode = 1;

% test invKin3D
broyden = invKin3D(l, theta0, desired, n, 0)';

newton = invKin3D(l, theta0, desired, n, 1)';

% it stops converging when there is no solution for sk, namely when the
% jacobian is singular. Since it is singular when the arm was straight and
% stretched out, as the point goes further and further away it will become
% singular and fail to converge.

% b)
% we can draw a curve from the end effector to the target and do a bezier
% towards the target. The smaller movements would prevent the jacobian from
% being singular.

% c) the issue is that similar to the answer in part one if the arm ever
% stretches straight it will fail to converge. We will try to avoid this
% problem by using a bezier to have the arm stay bent as it traverses in
% small sections towards the target.

% run in opposite quadrant
newtonBounds = invKin3D(l, theta0, oppQuad, n, 1)';

%%% PRINT IT ALL OUT %%%
fprintf('Broydens\n');
disp(broyden);

fprintf('Newtons\n');
disp(newton);

fprintf('Opposite Quadrant')
disp(newtonBounds);

plotRobot3D(l, newtonBounds);