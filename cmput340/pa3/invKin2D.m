function theta = invKin2D(l, theta0, pos, n, mode)
if mode == 1
    % Newton's method
    xk = theta0;    
    for k = 1:n
            % get the jacobian and current position
            [currPos, J] = evalRobot2D(l, xk);
            % calculate the difference
            f = currPos - pos;
            fnorm = norm(f);
            % if norm is under threshold return it
            if fnorm < 0.001
                theta = xk;
                return
            end
            sk = (-J)\f;
            xk = xk + sk;
    end
    % return what we get
    theta = xk;
    return
elseif mode == 0
    % Broyden's
    xk = theta0;
    % get starting jacobian
    [~, bk] = evalRobot2D(l, xk);
    for k = 1:n
        [currPos, ~] = evalRobot2D(l, xk);
        % get difference
        f = currPos - pos;
        fnorm = norm(f);
            % if norm is under threshold return it
            if fnorm < 0.001
                theta = xk;
                return
            end
        sk = (bk*-1)\f;
        xk = xk + sk;
        [currPos1, ~] = evalRobot2D(l, xk);
        % get the difference of xk+1
        f1 = currPos1 - pos;
        yk = f1 - f;
        bk = bk + ((yk - bk*sk)*sk')/(sk'*sk);
    end
    theta = xk;
end

% Q1 4): For positions that are out of reach of the arm, Newton's method
% will sometimes go to the max range the arm can reach or sometimes a
% seemingly random other position. Broyden's method however will error out.