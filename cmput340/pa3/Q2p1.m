l = [0.8;0.7];
%for bent arm: plotRobot3D([1 1],[pi/2,pi/2,2*pi])
thetaB = [pi/2; pi/2; 2*pi];
[~, J] = evalRobot3D(l, thetaB);
condB = cond(J) %condition number= 2.4915
detB = det(J) %determinant= 0.3920
%for straight arm: plotRobot3D([1 1],[pi/2,2*pi,2*pi])
thetaS = [pi/2; 2*pi; 2*pi];
[~, J] = evalRobot3D(l, thetaS);
condS = cond(J) %1.9977e+16
detS = det(J) %3.6114e-32

%since the determinant of the straight arm jacobian is close to 0, that
%jacobian is singular. A different theta vector is [5*pi/2; 6*pi; 6*pi],
%where all the angles are increased by 360 degrees, effectively resulting
%in the same positions