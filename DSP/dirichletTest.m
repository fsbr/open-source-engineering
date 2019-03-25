% might actually b pretty cool
w = 0:0.0001:pi;
y = diric(w,11)


% testing this thing:

% ./ made a huuuuge difference here
y1 = (sin(11*w/2))./(11*sin(w/2))
figure;
subplot(2,1,1)
plot(w,abs(y))
title('using the diric command')
xlabel('normalized radian frequency')
% im pretttty sure theres a way to get latex bindings in here
ylabel('|H(e^jw)|')
subplot(2,1,2)
plot(w,abs(y1))
title('using the actual equation')
xlabel('normalized radian frequency')
% im pretttty sure theres a way to get latex bindings in here
ylabel('|H(e^jw)|')
