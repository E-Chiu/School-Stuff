function theta = invKin3D(l,theta0,desired,n,mode)
if mode == 1
    % Newton's method
    xk = theta0;    
    for k = 1:n
            % get the jacobian and current position
            [currPos, J] = evalRobot3D(l, xk);
            % calculate the difference
            f = currPos' - desired;
            fnorm = norm(f);
            % if norm is under threshold return it
            if fnorm < 0.001
                theta = xk;
                return
            end
            sk = (J*-1)\f;
            xk = xk + sk;
    end
    % return what we get
    theta = xk;
    return
elseif mode == 0
    % Broyden's
    xk = theta0;
    % get starting jacobian
    [~, bk] = evalRobot3D(l, xk);
    for k = 1:n
        [currPos, ~] = evalRobot3D(l, xk);
        % get difference
        f = currPos' - desired;
        fnorm = norm(f);
            % if norm is under threshold return it
            if fnorm < 0.001
                theta = xk;
                return
            end
        sk = (bk*-1)\f;
        xk = xk + sk;
        [currPos1, ~] = evalRobot3D(l, xk);
        % get the difference of xk+1
        f1 = currPos1' - desired;
        yk = f1 - f;
        bk = bk + ((yk - bk*sk)*sk')/(sk'*sk);
    end
    theta = xk;
end