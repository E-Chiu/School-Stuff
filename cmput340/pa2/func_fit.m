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
    elseif basis == "trig"
        if rem(degrees, 2) == 1
            k = (degrees+1)/2;
        else
            k = floor((degrees-1)/2);
        end
        % form the 2 submatrices
            cosk = [cos(X.')];
            sink = [sin(X.')];
        for degree = 2:k
            cosk = [cosk cos(degree*X.')];
            sink = [sink sin(degree*X.')];
        end
        % put it all together
        A = [A cosk sink];
    end
    % solve linear system
    coefficient_vector = A\Y.';
end