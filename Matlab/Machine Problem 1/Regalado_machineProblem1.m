N = 1000;
t = (0:1/N:1-1/N);
x = 0;
x1 = 0;
A = 1; 
f0 = 10;
f01 = 10;
f = 1;
f1 = 1;

for k = 1:1:5
    %x + A*(4/pi)*((sin(2*pi*(2*k-1)*f0*t))/(2*k-1));
    %x + sin(k*t)/k;
    x = x + ((sin((2*pi)*((2*k)-1)*(f0*t)))/((2*k)-1));
end
    x = x * A * (4/pi);
    
figure;
plot(t,x);
title('k = 1 to 5');
xlabel('time in ms');
ylabel('y(t)');

for k1 = 1:1:10
    x1 = x1 + ((sin((2*pi)*((2*k1)-1)*(f01*t)))/((2*k1)-1));
end
    x1 = x1 * A * (4/pi);
    
figure;
plot(t,x1);
title('k = 1 to 10');
xlabel('time in ms');
ylabel('y(t)');

