% Sample script  that shows how to automate running problem solutions
close all;
clear;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% a) Load an image using the imread command 

peppers = imread('peppers3.tif');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% b) Display original image in the first spot of a 2 x 3 a grid layout
%    Check the imshow and subplot commands.

subplot(2,3,1);
imshow(peppers);
title('Original peppers image');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% c) Display a gray scale version of the image in position 2 of the grid.
%    help rgb2gray

grayPeppers = im2gray(peppers);
subplot(2,3,2);
imshow(grayPeppers);
title('GreyScale peppers image');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% d) Generate a new figure and ask user to manually select a region of the
%    image. Display the subimage in position 3 of the grid.
%    Hint 1: getrect()
%    Hint 2: to use getrect, you should first install Image Processing Toolbox:
%         (a) Open the Add-On Manager in MATLAB via "Home > Add-Ons > Get Add-Ons" and install the Add-On Explorer if it is not already installed.
%         (b) Search "Image Processing Toolbox" and install it.
%         (c) Restart MATLAB after installing

% Get user input on a newly dislayed image
f = figure;
imshow(peppers);
rect = getrect;
% Make grid the current figure
close(f)
subplot(2,3,3);
% Display selected region. Make sure to apply the cut
% over all 3 channels.
subRect = peppers(rect(2) : rect(2)+rect(4), rect(1) : rect(1)+rect(3), :);
imshow(subRect);
title('Selected region');

% You are NOT ALLOWED to use the imcrop function of Matlab.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% e) Create a function J = luminance_change(I, option, value) such that:
%   * When given the option 'c', the contrast of image I's top-left and 
%     bottom-right quadrants will be modified by the given value.
%     Simple multiplication will achieve this.
%   * When given the option 'b', the brightness of image I's top-right and 
%     bottom-left quadrants will be modified by the given value.
%     Simple addition will achieve this.
%  
%   Showcase your function by filling positions 4 and 5 in the grid

% Contrast change
subplot(2,3,4);
[cQ1, cQ3, cQ2, cQ4] = luminance_change(peppers, 'c', 0.5);
montage({cQ1, cQ2, cQ3, cQ4})
title('Reduced contrast');

% Brightness change
subplot(2,3,5);
[bQ1, bQ3, bQ2, bQ4] = luminance_change(peppers, 'b', 50);
montage({bQ1, bQ2, bQ3, bQ4})
title('Increased brightness');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% f) BONUS: Display a version of the image after it's been blurred using a
%    Gaussian filter. Hint: imgaussfilt()

subplot(2,3,6);
pepperGaussian = imgaussfilt(peppers, 5);
imshow(pepperGaussian);
title('GaussianBlur')

function [Q1, Q2, Q3, Q4] = luminance_change(I, option, value)
    % split into quadrants
    Q1 = I(1:size(I,1)/2, 1:size(I,2)/2,:);
    Q2 = I(size(I, 1)/2+1:size(I,1), 1:size(I,2)/2,:);
    Q3 = I(1:size(I,1)/2, size(I,2)/2+1:size(I,2),:);
    Q4 = I(size(I,1)/2+1:size(I,1), size(I,2)/2+1:size(I,2),:);

    % perform needed operation
    if option == 'c'
        Q1 = Q1 * value;
        Q4 = Q4 * value;
    end
    if option == 'b'
        Q2 = Q2 + value;
        Q3 = Q3 + value;
    end
end