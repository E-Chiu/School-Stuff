% a)
desired = [0; 3; 2];
l = [1;1];
n = 1000;
theta0 = [pi/2;pi/2;2*pi];
mode = 0;

invKin3D(l, theta0, desired, n, mode);

% it stops converging when there is no solution for sk, namely when the
% jacobian is singular. Since it is singular when the arm was straight and
% stretched out, as the point goes further and further away it will become
% singular and fail to converge.

% b)
% we can draw a curve from the end effector to the target and do a bezier
% towards the target. The smaller movements would prevent the jacobian from
% being singular.

% c)
steps = 6;
[start, ~] = evalRobot3D(l, theta0);
for s = 1:steps
    pos = bezier(start, desired, steps, s);
    invKin3D(l, theta0, desired, n, mode);
end

% borrowing the bezier question from Q2p3
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