% MMSE / Wiener Filter Lab - Version 1
% Self-contained MATLAB Online version
% Real-valued case, filter length N = 3

clear; clc; close all;

% ------------------------------------------------------------
% Project/data setup
% ------------------------------------------------------------

rootDir = pwd;
dataDir = fullfile(rootDir, 'data');

if ~exist(dataDir, 'dir')
    mkdir(dataDir);
end

disp('Current MATLAB folder:');
disp(rootDir);

disp('Using data directory:');
disp(dataDir);

% ------------------------------------------------------------
% Generate training data
% ------------------------------------------------------------

rng(7);          % Same idea as np.random.seed(7)
N = 3;           % Filter length
numSamples = 1000;

% True 3-tap system/channel
h_true = [0.7; -0.4; 0.2];

% Generate real-valued input signal
x = randn(numSamples, 1);

% Generate desired signal:
% d(n) = 0.7x(n) - 0.4x(n-1) + 0.2x(n-2) + noise
noiseStd = 0.05;
d = zeros(numSamples, 1);

for n = N:numSamples
    x_vec = [x(n); x(n-1); x(n-2)];
    d(n) = h_true.' * x_vec + noiseStd * randn();
end

% ------------------------------------------------------------
% Build data matrix X
% ------------------------------------------------------------
% Each row is:
%   [x(n), x(n-1), x(n-2)]

M = numSamples - N + 1;
X = zeros(M, N);

row = 1;
for n = N:numSamples
    X(row, :) = [x(n), x(n-1), x(n-2)];
    row = row + 1;
end

d_valid = d(N:end);

% ------------------------------------------------------------
% Estimate R and P
% ------------------------------------------------------------
% R = E[X(n)X^T(n)]
% P = E[X(n)d(n)]

R = (X.' * X) / M;
P = (X.' * d_valid) / M;

% ------------------------------------------------------------
% Solve Wiener-Hopf equation
% ------------------------------------------------------------
% Theoretical:
%   Wopt = R^{-1}P
%
% Numerical:
%   Solve R Wopt = P

W_matlab = R \ P;

% ------------------------------------------------------------
% Compute output and error
% ------------------------------------------------------------

y = X * W_matlab;
e = d_valid - y;

mse = mean(e.^2);
Ed2 = mean(d_valid.^2);
xi_min_formula = Ed2 - P.' * W_matlab;

% ------------------------------------------------------------
% Save generated data and MATLAB result
% ------------------------------------------------------------

writematrix(x, fullfile(dataDir, 'input_signal.csv'));
writematrix(d, fullfile(dataDir, 'desired_signal.csv'));
writematrix(R, fullfile(dataDir, 'R_matrix.csv'));
writematrix(P, fullfile(dataDir, 'P_vector.csv'));
writematrix(W_matlab, fullfile(dataDir, 'weights_matlab.csv'));
writematrix(y, fullfile(dataDir, 'output_matlab.csv'));
writematrix(e, fullfile(dataDir, 'error_matlab.csv'));

% ------------------------------------------------------------
% Display results
% ------------------------------------------------------------

disp(' ');
disp('MMSE Wiener Filter Lab - MATLAB Self-Contained Demo');
disp('--------------------------------------------------');

disp('True system h:');
disp(h_true);

disp('Autocorrelation matrix R:');
disp(R);

disp('Cross-correlation vector P:');
disp(P);

disp('Estimated Wiener weights from MATLAB:');
disp(W_matlab);

disp('Condition number of R:');
disp(cond(R));

fprintf('MSE from actual error:      %.8f\n', mse);
fprintf('MMSE formula Ed2 - P^T W:   %.8f\n', xi_min_formula);

% ------------------------------------------------------------
% Plot desired signal and filter output
% ------------------------------------------------------------

figure;
plot(d_valid, 'LineWidth', 1.0);
hold on;
plot(y, '--', 'LineWidth', 1.0);
grid on;
xlabel('Sample index');
ylabel('Amplitude');
title('Desired signal d(n) vs Wiener filter output y(n)');
legend('Desired signal d(n)', 'Filter output y(n)');

% ------------------------------------------------------------
% Plot error
% ------------------------------------------------------------

figure;
plot(e, 'LineWidth', 1.0);
grid on;
xlabel('Sample index');
ylabel('Error amplitude');
title('Estimation error e(n) = d(n) - y(n)');