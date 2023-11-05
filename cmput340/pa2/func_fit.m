function [coefficient_vector] = func_fit(X,Y,type,basis,parameters)
    if type == "interpolate"
        degrees = size(X,2)-1;
    elseif type == "approximate"
        degrees = parameters;
    end
    % create the A matrix
    % start off with column of ones
    A = [ones(size(X, 2), 1)];
    if basis == "poly"
        for degree = 1:degrees
            % concatenate t^degree
            A = [A (X.^degree).'];
        end
        A = fliplr(A);
    elseif basis == "trig"
        % get K
        if rem(degrees, 2) == 1
            % if odd number of points K=(n-1)/2
            K = (degrees-1)/2
        else
            K = floor((degrees-1)/2)
        end
        % form the 2 submatrices
            cosk = [];
            sink = [];
        for degree = 1:K
            cosk = [cosk cos(degree*X')];
            sink = [sink sin(degree*X')];
        end
        % put it all together
        A = [A cosk sink];
        if rem(degrees, 2) == 0
            % if it was even add additional basis
            A = [A sin((K+1)*X')];
        end
    end
    % solve linear system
    coefficient_vector = A\Y';
end