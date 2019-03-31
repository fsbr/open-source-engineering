% making the homework solution
clear all;
close all;
% make a controller object
G = zpk([], [0 -4 -6],[1])

% plot the root locus against whatever values of k we want
k = 0:0.01:300;
% plot the root locus
figure;
rlocus(G,k)

% search on the 16% overshoot line
% gain K = 43.4
% Pole location is -1.2 +/- 2.07j

% current step response
% put it into unity feedback
K = 44.4
Gcl = feedback(K*G,1)
figure;
step(Gcl)

%Ts = 4/sigma 
% 4/1.2 = 3.33
% Ts_goal = 1.11
%Ts_goal = 4/sigma
%sigma = 4/Ts_goal
%sigma = 3.603

% desired pole location is 
% sigma = 3.603
% wd = 6.21
Gcompensated = zpk([-3.006], [0 -4 -6],[1])
figure;
rlocus(Gcompensated,k)
% gain 49.3

% take the step response:
%put it into feedback
Kc = 47.6
figure;
Gcomp_cl = feedback(Kc*Gcompensated,1);
step(Gcomp_cl)

figure;
%with both step responses together
step(Gcl)
hold on
step(Gcomp_cl)
xlabel('time')
ylabel('unit')
title('PD controller design')
