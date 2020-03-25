%Kent Regalado - 11443812

%I do hereby affirm, on my honor as a student, 
%at the submission of this machine exercise 
%that the work I am submitting is my own
%and was not copied or done with others.

clc;

prompt = 'How many numbers would you like to enter? (max 20):';
ctr = input(prompt)

x = [];
for i = 1:ctr
    x(i) = input('Input a number:')
end

dtmf_sig(x);

function dtmf = dtmf_sig(x)
A = 2;
N = 10000;
t = (0:1/N:0.2);
y = [];
res = [];

[y,fs] = audioread('4143397.wav'); 

for i = 1:numel(x)
    opt = x(i);
if opt == 1
    f0 = 1209;
    f1 = 697;
    y1 = A*sin(2*pi*f0*t);
    y2 = A*sin(2*pi*f1*t);
    y = y1 + y2;
elseif opt == 2
    f0 = 1336;
    f1 = 697;
    y1 = A*sin(2*pi*f0*t);
    y2 = A*sin(2*pi*f1*t);
    y = y1 + y2;
elseif opt == 3
    f0 = 1477;
    f1 = 697;
    y1 = A*sin(2*pi*f0*t);
    y2 = A*sin(2*pi*f1*t);
    y = y1 + y2;
elseif opt == 4
    f0 = 1209;
    f1 = 697;
    y1 = A*sin(2*pi*f0*t);
    y2 = A*sin(2*pi*f1*t);
    y = y1 + y2;
elseif opt == 5
    f0 = 1336;
    f1 = 697;
    y1 = A*sin(2*pi*f0*t);
    y2 = A*sin(2*pi*f1*t);
    y = y1 + y2;
elseif opt == 6
    f0 = 1477;
    f1 = 697;
    y1 = A*sin(2*pi*f0*t);
    y2 = A*sin(2*pi*f1*t);
    y = y1 + y2;
elseif opt == 7
    f0 = 1209;
    f1 = 697;
    y1 = A*sin(2*pi*f0*t);
    y2 = A*sin(2*pi*f1*t);
    y = y1 + y2;
elseif opt == 8
    f0 = 1336;
    f1 = 697;
    y1 = A*sin(2*pi*f0*t);
    y2 = A*sin(2*pi*f1*t);
    y = y1 + y2;
elseif opt == 9
    f0 = 1477;
    f1 = 697;
    y1 = A*sin(2*pi*f0*t);
    y2 = A*sin(2*pi*f1*t);
    y = y1 + y2;
elseif opt == 10
    f0 = 1209;
    f1 = 697;
    y1 = A*sin(2*pi*f0*t);
    y2 = A*sin(2*pi*f1*t);
    y = y1 + y2;
elseif opt == 11
    f0 = 1336;
    f1 = 697;
    y1 = A*sin(2*pi*f0*t);
    y2 = A*sin(2*pi*f1*t);
    y = y1 + y2;
elseif opt == 12
    f0 = 1477;
    f1 = 697;
    y1 = A*sin(2*pi*f0*t);
    y2 = A*sin(2*pi*f1*t);
    y = y1 + y2;
end

res = [res y];

soundsc(res, fs);
end
end