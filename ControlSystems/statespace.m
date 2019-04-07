% okay
clear all;
close all;
G = zpk([-5],[0 -1 -4],[1])
k = 0:0.01:500;
figure;
rlocus(G,k)

% -0.48 + j0.641
Gcl = feedback(0.518*G,1)

figure;
step(Gcl)

% testing values
z = (-log(0.095))/(sqrt(pi^2 + log(0.095)^2))
wn = 4/0.74 % wn =5.4
