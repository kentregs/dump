%Kent Regalado - 11443812

%I do hereby affirm, on my honor as a student, 
%at the submission of this machine exercise 
%that the work I am submitting is my own
%and was not copied or done with others.

clc;

N = 10000;
t = (0:1/N:1-1/N);
saw = zeros(size(t));
revsaw = zeros(size(t));
prompt = 'Enter value for f0:'
f0 = input(prompt)
prompt = 'Enter value for A:'
A = input(prompt)
prompt = 'Enter value for k:'
k = input(prompt)

for k = 1:5
    saw = saw + (((-1)^k)*(sin(2*pi*k*f0*t)/k));
end
    saw = (A/2) - (A/pi) * saw;
 
figure;
plot(t,saw);
title('Sawtooth signal');
xlabel('time in s');
ylabel('y(t)');

