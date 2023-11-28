function theta = invKin2D(l, theta0, pos, n, mode)
if mode == 1
    xk = theta0;    
    for k = 1:n
            [currPos, J] = evalRobot2D(l, xk);
            f = currPos - pos;
            fnorm = norm(f);
            if fnorm < 0.001
                theta = xk;
                return
            end
            sk = (J*-1)\f';
            xk = xk + sk;
    end
    theta = xk;
    return
elseif mode == 0
    xk = theta0;
    [~, bk] = evalRobot2D(l, xk);
    for k = 1:n
        [currPos, ~] = evalRobot2D(l, xk);
        f = currPos - pos;
        fnorm = norm(f);
            if fnorm < 0.001
                theta = xk;
                return
            end
        sk = (bk*-1)\f';
        xk = xk + sk;
        [currPos1, ~] = evalRobot2D(l, xk);
        f1 = currPos1 - pos;
        yk = f1 - f;
        bk = bk + ((yk - bk*sk)*sk')/(sk'*sk);
    end
    theta = xk;
end