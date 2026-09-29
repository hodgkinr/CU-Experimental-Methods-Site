%% ASEN 3501 Tier 2 power-lab example
% This script creates presentation-quality plots for the resistance-sweep
% example used in the Tier 2 normalized-uncertainty guide.
%
% The manufacturer half-widths and fixed sensor terms below are illustrative
% values selected for this bridge example. Replace them with the specifications
% supplied for the actual power-lab instruments.
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

%% Manufacturer half-width plus fixed sensor contribution model
% h_x is the manufacturer half-width expressed as a fraction of reading.
% d_x is an illustrative fixed half-width representing contributions such
% as resolution, digitization, and a reading-independent sensor floor.
% Both terms are treated as rectangular contributions, so the corresponding
% standard uncertainty is the root-sum-square divided by sqrt(3).
hV = 0.005 / 100;                                % voltmeter, fraction of reading
hI = 0.060 / 100;                                % ammeter, fraction of reading
hR = 0.012 / 100;                                % ohmmeter, fraction of reading
dV = 0.0025;                                     % voltmeter fixed term [V]
dI = 0.0005;                                     % ammeter fixed term [A]
dR = 0.10;                                       % ohmmeter fixed term [ohm]

uV = sqrt((hV .* abs(V)).^2 + dV.^2) / sqrt(3);
uI = sqrt((hI .* abs(I)).^2 + dI.^2) / sqrt(3);
uR = sqrt((hR .* abs(R)).^2 + dR.^2) / sqrt(3);

bV = uV .* abs(V);
bI = uI .* abs(I);
bR = uR .* abs(R);

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

%% Monte Carlo resistance sweep
% The Monte Carlo curves use the same manufacturer and fixed half-widths
% as the Taylor-series uncertainty model. Each input receives two
% independent bounded uniform perturbations.
rng(3501, 'twister');
mcResistance = logspace(log10(10), log10(1000), 60);
mcSamples = 10000;
mcSSU = zeros(numel(mcResistance), 3);
mcNSU = zeros(numel(mcResistance), 3);
mcInputNSU = zeros(numel(mcResistance), 3);

for k = 1:numel(mcResistance)
    j = findClosestIndex(R, mcResistance(k));
    [mcSSU(k, :), mcNSU(k, :), mcInputNSU(k, :)] = monteCarloPower( ...
        V(j), I(j), R(j), hV, hI, hR, dV, dI, dR, mcSamples);
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
    plot(ax, mcResistance, mcSSU(:, k), 'o', 'Color', theme.plotColors(k, :), ...
        'MarkerFaceColor', theme.plotColors(k, :), 'MarkerSize', 4.5, ...
        'LineStyle', 'none', 'HandleVisibility', 'off');
end
styleAxes(ax, theme);

title(ax, {'Scaled systematic standard uncertainty in power', ...
    'Taylor-series curves with Monte Carlo checks'}, ...
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
plot(ax, mcResistance, mcInputNSU(:, 1), 'o', 'Color', theme.plotColors(1, :), ...
    'MarkerFaceColor', theme.plotColors(1, :), 'MarkerSize', 4.5, ...
    'LineStyle', 'none', 'HandleVisibility', 'off');
plot(ax, mcResistance, mcInputNSU(:, 2), 'o', 'Color', theme.plotColors(2, :), ...
    'MarkerFaceColor', theme.plotColors(2, :), 'MarkerSize', 4.5, ...
    'LineStyle', 'none', 'HandleVisibility', 'off');
plot(ax, mcResistance, mcInputNSU(:, 3), 'o', 'Color', theme.plotColors(3, :), ...
    'MarkerFaceColor', theme.plotColors(3, :), 'MarkerSize', 4.5, ...
    'LineStyle', 'none', 'HandleVisibility', 'off');
styleAxes(ax, theme);

title(ax, {'Normalized systematic standard uncertainty of measured inputs', ...
    'Taylor-series curves with Monte Carlo checks'}, ...
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
    plot(ax, mcResistance, mcNSU(:, k), 'o', 'Color', theme.plotColors(k, :), ...
        'MarkerFaceColor', theme.plotColors(k, :), 'MarkerSize', 4.5, ...
        'LineStyle', 'none', 'HandleVisibility', 'off');
end

illustrativeThreshold = 0.0005;
yline(ax, illustrativeThreshold, '-.', 'Illustrative 0.05% threshold', ...
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
    'Location', 'northwest', 'Box', 'off', 'FontSize', theme.legendSize);
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

function [ssu, nsu, inputNsu] = monteCarloPower( ...
        V, I, R, hV, hI, hR, dV, dI, dR, N)
% Use independent bounded uniform perturbations for the proportional and
% fixed contributions. This matches the Taylor-series standard uncertainty
% model, which divides the combined half-width by sqrt(3).
uniformDraw = @(n) (2 * rand(n, 1) - 1);
Vstar = V + hV * abs(V) * uniformDraw(N) + dV * uniformDraw(N);
Istar = I + hI * abs(I) * uniformDraw(N) + dI * uniformDraw(N);
Rstar = R + hR * abs(R) * uniformDraw(N) + dR * uniformDraw(N);

P1star = Vstar .* Istar;
P2star = Istar.^2 .* Rstar;
P3star = Vstar.^2 ./ Rstar;

ssu = [std(P1star), std(P2star), std(P3star)];
nominalPower = [V * I, I^2 * R, V^2 / R];
nsu = ssu ./ abs(nominalPower);
inputNsu = [std(Vstar) / abs(V), std(Istar) / abs(I), std(Rstar) / abs(R)];
end
