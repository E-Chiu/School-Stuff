l = [1;1];
%for bent arm: plotRobot3D([1 1],[pi/2,pi/2,2*pi])
thetaB = [pi/2; pi/2; 2*pi];
[~, J] = evalRobot3D(l, thetaB);
condB = cond(J) %condition number= 2.6180
detB = det(J) %determinant= 1
%for straight arm: plotRobot3D([1 1],[pi/2,2*pi,2*pi])
thetaS = [pi/2; 2*pi; 2*pi];
[~, J] = evalRobot3D(l, thetaS);
condS = cond(J) %2.0414e+16
detS = det(J) %8.9986e-32

%since the determinant of the straight arm jacobian is close to 0, that
%jacobian is singular. A different theta vector is [5*pi/2; 6*pi; 6*pi],
%where all the angles are increased by 360 degrees, effectively resulting
%in the same positions