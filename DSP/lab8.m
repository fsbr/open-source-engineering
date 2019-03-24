% in this lab we're going to implement the bandpass filter over a given image
clear all;
close all;
clc;
A = imread('homework.png');

% indexes from top left
% get the 99th row and plot it just like in the book
% so the plot is the index on the horizontal the pixel value vert.
y = (A(99,:))
x = 1:length(y);
figure;
plot(x,y)
xlabel('column index (n)')
ylabel('pixel value 0-255')

% theres two ways to compute the 11 point moving average filter
% convolution way
a = ones(11,1)/11
y1 = conv(a,y);

% val vs low pass val
figure;
subplot(2,1,1)
plot(y,'b')
title('99th row, original data')
xlabel('index (n)')
ylabel('pixel value')
hold on
subplot(2,1,2)
plot(y1,'r')
title('99th row, filtered data (11 point moving average)')
xlabel('index (n)')
ylabel('pixel value')

% do the entire image
for i = 1:length(A(:,1))
    outimage(i,:) = conv(a,A(i,:));
end

figure;
subplot(2,1,1)
imshow(A)
subplot(2,1,2)
imshow(outimage,[])
