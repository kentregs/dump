s = input('Please enter your telephone number: ', 's');
n = length(s);
sample_rate = 32768;
t = 1/sample_rate;
time_vector = [0:t:0.25];
for i = 1:n
    switch s(i)
        case '0'
            f_low = 941;
            f_high = 1336;
            y_low = 0.5*sin(2*pi*f_low*time_vector);
            y_high = 0.5*sin(2*pi*f_high*time_vector);
            y = y_low + y_high;
            figure(i);
            plot(time_vector, y), axis([0, 0.01, -1, 1]);
            xlabel('t'), ylabel('y');
        case '1'
            f_low = 697;
            f_high = 1209;
            y_low = 0.5*sin(2*pi*f_low*time_vector);
            y_high = 0.5*sin(2*pi*f_high*time_vector);
            y = y_low + y_high;
            figure(i);
            plot(time_vector, y), axis([0, 0.01, -1, 1]);
            xlabel('t'), ylabel('y');
        case '2'
            f_low = 697;
            f_high = 1336;
            y_low = 0.5*sin(2*pi*f_low*time_vector);
            y_high = 0.5*sin(2*pi*f_high*time_vector);
            y = y_low + y_high;
            figure(i);
            plot(time_vector, y), axis([0, 0.01, -1, 1]);
            xlabel('t'), ylabel('y');
        case '3'
            f_low = 697;
            f_high = 1477;
            y_low= 0.5*sin(2*pi*f_low*time_vector);
            y_high = 0.5*sin(2*pi*f_high*time_vector);
            y = y_low + y_high;
            figure(i);
            plot(time_vector, y), axis([0, 0.01, -1, 1]);
            xlabel('t'), ylabel('y');
        case '4'
            f_low = 770;
            f_high = 1209;
            y_low = 0.5*sin(2*pi*f_low*time_vector);
            y_high = 0.5*sin(2*pi*f_high*time_vector);
            y = y_low + y_high;
            figure(i);
            plot(time_vector, y), axis([0, 0.01, -1, 1]);
            xlabel('t'), ylabel('y');
        case '5'
            f_low = 770;
            f_high = 1336;
            y_low = 0.5*sin(2*pi*f_low*time_vector);
            y_high = 0.5*sin(2*pi*f_high*time_vector);
            y = y_low + y_high;
            figure(i);
            plot(time_vector, y), axis([0, 0.01, -1, 1]);
            xlabel('t'), ylabel('y');
        case '6'
            f_low = 770;
            f_high = 1477;
            y_low = 0.5*sin(2*pi*f_low*time_vector);
            y_high = 0.5*sin(2*pi*f_high*time_vector);
            y = y_low + y_high;
            figure(i);
            plot(time_vector, y), axis([0, 0.01, -1, 1]);
            xlabel('t'), ylabel('y');
        case '7'
            f_low = 852;
            f_high = 1209;
            y_low = 0.5*sin(2*pi*f_low*time_vector);
            y_high = 0.5*sin(2*pi*f_high*time_vector);
            y = y_low + y_high;
            figure(i);
            plot(time_vector, y), axis([0, 0.01, -1, 1]);
            xlabel('t'), ylabel('y');
        case '8'
            f_low = 852;
            f_high = 1336;
            y_low = 0.5*sin(2*pi*f_low*time_vector);
            y_high = 0.5*sin(2*pi*f_high*time_vector);
            y = y_low + y_high;
            figure(i);
            plot(time_vector, y), axis([0, 0.01, -1, 1]);
            xlabel('t'), ylabel('y');
        case '9'
            f_low = 852;
            f_high = 1477;
            y_low = 0.5*sin(2*pi*f_low*time_vector);
            y_high = 0.5*sin(2*pi*f_high*time_vector);
            y = y_low + y_high;
            figure(i);
            plot(time_vector, y), axis([0, 0.01, -1, 1]);
            xlabel('t'), ylabel('y');
    end
end
