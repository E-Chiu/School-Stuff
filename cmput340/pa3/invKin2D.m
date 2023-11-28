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
            sk = -J\f;
            xk = xk + sk;
    end
    theta = xk;
    return
elseif mode == 0

end