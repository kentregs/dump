[y1,fs] = audioread('y_1.wav'); 
[y2,fs] = audioread('y_2.wav'); 
[y3,fs] = audioread('y_3.wav'); 
[y4,fs] = audioread('y_4.wav'); 
[y5,fs] = audioread('y_5.wav'); 
[y6,fs] = audioread('y_6.wav'); 
[y7,fs] = audioread('y_7.wav'); 
[y8,fs] = audioread('y_8.wav'); 
[y9,fs] = audioread('y_9.wav'); 
[y10,fs] = audioread('y_10.wav'); 

% y1 to y10 have the same specs:
% NumChannels:  1
% SampleRate:   16000
% TotalSamples: 25507
% Duration:     1.5942 
% BitsPerSample:16

y_clean = (y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10) / 10;

coeff = ones(1,10)/10;
avg10 = filter(coeff, 1, y_clean);

%sound(y1);
%sound(y_clean);
sound(avg10);

audiowrite('y_clean.wav', avg10, fs);
