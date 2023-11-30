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
% problem by using a bezier.

% run without breaking up
newtonBounds = invKin3D(l, theta0, oppQuad, n, 1)';

% with bezier
steps = 10;
[start, ~] = evalRobot3D(l, theta);
answer = [];
for s = 1:steps
    pos = bezier(start, oppQuad, steps, s);
    res = invKin3D(l, theta0, pos, n, mode);
    answer = [answer res'];
end
newtonBezier = answer;

%%% PRINT IT ALL OUT %%%
fprintf('Broydens\n');
disp(broyden);

fprintf('Newtons\n');
disp(newton);

fprintf('Newtown out of bounds\n');
disp(newtonBounds);

fprintf('Newtown with bezier\n');
disp(newtonBezier);

% borrowing the bezier function from Q2p3
function desired = bezier(start_pos, end_pos, steps, curr_segment)
    %The trajectory smoothly varies between:
    %   1. start point
    %   2. start point + vertical offset
    %   3. end point + vertical offset
    %   4. end point
    arr_steps = linspace(0, 1, steps);
    tb = arr_steps(curr_segment);
    start_ver = start_pos;
    start_ver(3) = 1.5;
    end_ver = end_pos;
    end_ver(3) = 1.5;
    bez1 = (1-tb)*((1-tb)*start_pos+tb*start_ver) + tb*((1-tb)*start_ver + tb*end_ver);
    bez2 = (1-tb)*((1-tb)*start_ver + tb*end_ver) + tb*((1-tb)*end_ver + tb*end_pos);
    desired = (1-tb)*bez1 + tb*bez2;
end

% answer from newton: plotRobot3D([.8 .7],[0.5657 -0.0000 1.2657])
% final column of bezier: plotRobot3D([.8 .7],[-2.3569 7.0699 6.2832])