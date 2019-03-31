% okay so we're moving to matlab
G = zpk([],[0 -7],[1])
k = 0:0.001:100;
rlocus(G,k)

