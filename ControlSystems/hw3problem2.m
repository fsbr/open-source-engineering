clear all;close all
% going for problem 2
G = zpk([],[0 -8 -25],[1])
k = 0:1:8e3;

rlocus(G,k)

% record the gain
K = 1.14e3;

% current pole location
% -2.91 + j5.77

%desired pole locations
sigma_goal = -2.91 * 4
wd_goal = 5.77*4

% og step response
Gcl = feedback(K*G,1)

% new step response
Gnew = zpk([-9.377],[0 -8 -25],[1])
figure;
rlocus(Gnew,k)

% i looked at the root locus to do this Knew value 
Knew = 692

Gnew_cl = feedback(Knew*Gnew,1)

figure;
step(Gcl)
hold on
step(Gnew_cl)
