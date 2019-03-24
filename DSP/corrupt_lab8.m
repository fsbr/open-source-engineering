clear all;
close all;
clc
A = imread('homework.png')

% we want to corrupt with the book noise
% x1[n] = x[n] + 128 + 128*cos(2pi n / 11)

n = 1:length(A(99,:))

% do it once
y = double(A(99,:))
y1 = y + 128 + 128*cos(2*pi*n/11)

subplot(2,1,1)
plot(y)
title('regular pixel value')
xlabel('index')
ylabel('pixel value')

subplot(2,1,2)
plot(y1)
title('corrupted pixel values')
xlabel('index')
ylabel('pixel value')

% do it for everything.
for i=1:length(A(:,1))
    outImg(i,:) = double(A(i,:)) + 128 + 128*cos(2*pi*n/11);
end

figure;
imshow(outImg,[])
imwrite(outImg/511,'noiseyImage.jpg')

