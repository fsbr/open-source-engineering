% what's expected of students code wise

% the "index plot"

% then 
clear all
close all
clc
A = imread('noiseyImage.jpg')

%build filter
L = 11 
b = ones(L,1)/L

for i=1:length(A(:,1))
    outImg(i,:) = conv(double(A(i,:)),b);
end

%please work
imshow(outImg,[])
