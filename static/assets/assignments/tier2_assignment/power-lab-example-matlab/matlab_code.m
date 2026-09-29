%% ASEN 3501 Tier 2 power-lab example
% This script creates presentation-quality plots for the resistance-sweep
% example used in the Tier 2 normalized-uncertainty guide.
%
% The instrument values below are illustrative placeholders. Replace them
% with the specifications supplied for the actual power-lab instruments.
%
% Outputs written to this folder:
%   scaled_systematic_uncertainty_vs_resistance.png
%   normalized_input_uncertainty_vs_resistance.png
%   normalized_power_uncertainty_vs_resistance.png

clear;
close all;
clc;

outputFolder = fileparts(mfilename('fullpath'));
theme = cuTheme();

%% Nominal power model
R = logspace(log10(10), log10(1000), 400);       % resistance [ohm]
V0 = 5.0;                                       % nominal source voltage [V]
V = V0 .* ones(size(R));                         % constant-voltage example
I = V ./ R;                                      % nominal current [A]

P1 = V .* I;                                     % P = V I
P2 = I.^2 .* R;                                  % P = I^2 R
P3 = V.^2 ./ R;                                  % P = V^2 / R

%% Illustrative systematic standard-uncertainty model
% a_x is the full width of a rectangular resolution interval.
% g_x is a proportional accuracy coefficient expressed as a fraction.
aV = 0.010;  gV = 0.005;                         % voltmeter [V], fraction
aI = 0.002;  gI = 0.010;                         % ammeter [A], fraction
aR = 0.50;   gR = 0.005;                         % ohmmeter [ohm], fraction

bV = sqrt((aV / sqrt(12)).^2 + (gV .* abs(V)).^2);
bI = sqrt((aI / sqrt(12)).^2 + (gI .* abs(I)).^2);
bR = sqrt((aR / sqrt(12)).^2 + (gR .* abs(R)).^2);

nV = bV ./ abs(V);
nI = bI ./ abs(I);
nR = bR ./ abs(R);

% Dimensionless sensitivity coefficients for the three power equations:
% P = V I       -> S_V = 1,  S_I = 1
% P = I^2 R     -> S_I = 2,  S_R = 1
% P = V^2 / R   -> S_V = 2,  S_R = -1
nsuP1 = sqrt(nV.^2 + nI.^2);
nsuP2 = sqrt((2 .* nI).^2 + nR.^2);
nsuP3 = sqrt((2 .* nV).^2 + nR.^2);

ssuP1 = abs(P1) .* nsuP1;                        % scaled uncertainty [W]
ssuP2 = abs(P2) .* nsuP2;
ssuP3 = abs(P3) .* nsuP3;

%% Pointwise Monte Carlo check
% The markers in the figures compare Monte Carlo estimates with the
% first-order Taylor-series curves at representative resistance values.
rng(3501, 'twister');
mcResistance = [25, 100, 400];                  % [ohm]
mcSamples = 20000;
mcSSU = zeros(numel(mcResistance), 3);
mcNSU = zeros(numel(mcResistance), 3);

for k = 1:numel(mcResistance)
    j = findClosestIndex(R, mcResistance(k));
    [mcSSU(k, :), mcNSU(k, :)] = monteCarloPower( ...
        V(j), I(j), R(j), aV, gV, aI, gI, aR, gR, mcSamples);
end

%% Plot 1: scaled systematic standard uncertainty in power
fig = presentationFigure([1050, 680]);
ax = axes(fig); %#ok<LAXES>
styleAxes(ax, theme);
axes(ax);
colororder(theme.plotColors);
set(ax, 'ColorOrder', theme.plotColors, 'ColorOrderIndex', 1);

h1 = loglog(ax, R, ssuP1, '-', 'LineWidth', 2.4);
hold(ax, 'on');
h2 = loglog(ax, R, ssuP2, '--', 'LineWidth', 2.4);
h3 = loglog(ax, R, ssuP3, ':', 'LineWidth', 2.8);

for k = 1:3
    scatter(ax, mcResistance, mcSSU(:, k), 72, theme.plotColors(k, :), ...
        'o', 'filled', 'MarkerEdgeColor', theme.black, ...
        'LineWidth', 0.8, 'HandleVisibility', 'off');
end
styleAxes(ax, theme);

title(ax, {'Scaled systematic standard uncertainty in power', ...
    'Illustrative constant-voltage resistance sweep'}, ...
    'FontSize', theme.titleSize, 'FontWeight', 'bold', 'Color', theme.black);
xlabel(ax, 'Resistance, R [\Omega]', 'Interpreter', 'tex', 'Color', theme.black);
ylabel(ax, 'Scaled systematic standard uncertainty, SSU_P [W]', ...
    'Interpreter', 'tex', 'Color', theme.black);
lgd = legend(ax, [h1, h2, h3], {'P = VI', 'P = I^2R', 'P = V^2/R'}, ...
    'Location', 'southwest', 'Box', 'off', 'FontSize', theme.legendSize);
lgd.TextColor = theme.black;
exportgraphics(fig, fullfile(outputFolder, ...
    'scaled_systematic_uncertainty_vs_resistance.png'), 'Resolution', 300);
close(fig);

%% Plot 2: normalized systematic standard uncertainty of V, I, and R
fig = presentationFigure([1050, 680]);
ax = axes(fig); %#ok<LAXES>
styleAxes(ax, theme);
axes(ax);
colororder(theme.plotColors);
set(ax, 'ColorOrder', theme.plotColors, 'ColorOrderIndex', 1);

h1 = loglog(ax, R, nV, '-', 'LineWidth', 2.4);
hold(ax, 'on');
h2 = loglog(ax, R, nI, '--', 'LineWidth', 2.4);
h3 = loglog(ax, R, nR, ':', 'LineWidth', 2.8);
styleAxes(ax, theme);

title(ax, {'Normalized systematic standard uncertainty of measured inputs', ...
    'Illustrative sensor model'}, ...
    'FontSize', theme.titleSize, 'FontWeight', 'bold', 'Color', theme.black);
xlabel(ax, 'Resistance, R [\Omega]', 'Interpreter', 'tex', 'Color', theme.black);
ylabel(ax, 'Normalized systematic standard uncertainty', ...
    'Interpreter', 'tex', 'Color', theme.black);
lgd = legend(ax, [h1, h2, h3], {'Voltage, V', 'Current, I', 'Resistance, R'}, ...
    'Location', 'best', 'Box', 'off', 'FontSize', theme.legendSize);
lgd.TextColor = theme.black;
exportgraphics(fig, fullfile(outputFolder, ...
    'normalized_input_uncertainty_vs_resistance.png'), 'Resolution', 300);
close(fig);

%% Plot 3: normalized systematic standard uncertainty of power
fig = presentationFigure([1050, 680]);
ax = axes(fig); %#ok<LAXES>
styleAxes(ax, theme);
axes(ax);
colororder(theme.plotColors);
set(ax, 'ColorOrder', theme.plotColors, 'ColorOrderIndex', 1);

h1 = loglog(ax, R, nsuP1, '-', 'LineWidth', 2.4);
hold(ax, 'on');
h2 = loglog(ax, R, nsuP2, '--', 'LineWidth', 2.4);
h3 = loglog(ax, R, nsuP3, ':', 'LineWidth', 2.8);

for k = 1:3
    scatter(ax, mcResistance, mcNSU(:, k), 72, theme.plotColors(k, :), ...
        'o', 'filled', 'MarkerEdgeColor', theme.black, ...
        'LineWidth', 0.8, 'HandleVisibility', 'off');
end

illustrativeThreshold = 0.05;
yline(ax, illustrativeThreshold, '-.', 'Illustrative 5% threshold', ...
    'Color', theme.darkGray, 'LineWidth', 1.4, ...
    'LabelHorizontalAlignment', 'right', 'FontSize', theme.annotationSize, ...
    'HandleVisibility', 'off');
styleAxes(ax, theme);

title(ax, {'Normalized systematic standard uncertainty in power', ...
    'Taylor-series curves with Monte Carlo checks'}, ...
    'FontSize', theme.titleSize, 'FontWeight', 'bold', 'Color', theme.black);
xlabel(ax, 'Resistance, R [\Omega]', 'Interpreter', 'tex', 'Color', theme.black);
ylabel(ax, 'NSU_{P,sys} = SSU_P / |P|', 'Interpreter', 'tex', 'Color', theme.black);
lgd = legend(ax, [h1, h2, h3], {'P = VI', 'P = I^2R', 'P = V^2/R'}, ...
    'Location', 'best', 'Box', 'off', 'FontSize', theme.legendSize);
lgd.TextColor = theme.black;
exportgraphics(fig, fullfile(outputFolder, ...
    'normalized_power_uncertainty_vs_resistance.png'), 'Resolution', 300);
close(fig);

disp(['Plots written to: ', outputFolder]);

%% Local functions
function theme = cuTheme()
% Centralized CU Boulder palette and shared presentation settings.
theme.black = [0, 0, 0];
theme.gold = [207, 184, 124] / 255;              % #CFB87C
theme.darkGray = [86, 90, 92] / 255;            % #565A5C
theme.lightGray = [0.88, 0.88, 0.88];
theme.plotColors = [theme.black; theme.gold; theme.darkGray];
theme.fontName = 'Helvetica';
theme.bodySize = 14;
theme.titleSize = 17;
theme.legendSize = 13;
theme.annotationSize = 11;
end

function fig = presentationFigure(position)
if numel(position) == 2
    position = [100, 100, position];
end
fig = figure('Color', 'white', 'Position', position, ...
    'InvertHardcopy', 'off', 'Renderer', 'painters');
end

function styleAxes(ax, theme)
set(ax, 'FontName', theme.fontName, 'FontSize', theme.bodySize, ...
    'LineWidth', 1.1, 'Box', 'off', 'TickDir', 'out', ...
    'Color', 'white', 'XColor', theme.black, 'YColor', theme.black, ...
    'ColorOrder', theme.plotColors, 'ColorOrderIndex', 1, ...
    'XMinorGrid', 'on', 'YMinorGrid', 'on', ...
    'GridColor', theme.lightGray, 'MinorGridColor', theme.lightGray, ...
    'GridAlpha', 0.8, 'MinorGridAlpha', 0.45);
grid(ax, 'on');
end

function index = findClosestIndex(values, target)
[~, index] = min(abs(values - target));
end

function [ssu, nsu] = monteCarloPower(V, I, R, aV, gV, aI, gI, aR, gR, N)
Vstar = V + gV * abs(V) * randn(N, 1) + (aV / 2) * (2 * rand(N, 1) - 1);
Istar = I + gI * abs(I) * randn(N, 1) + (aI / 2) * (2 * rand(N, 1) - 1);
Rstar = R + gR * abs(R) * randn(N, 1) + (aR / 2) * (2 * rand(N, 1) - 1);

P1star = Vstar .* Istar;
P2star = Istar.^2 .* Rstar;
P3star = Vstar.^2 ./ Rstar;

ssu = [std(P1star), std(P2star), std(P3star)];
nominalPower = [V * I, I^2 * R, V^2 / R];
nsu = ssu ./ abs(nominalPower);
end
