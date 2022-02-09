%% Example C from Lecture L3b:  Hermite splines
% Let's have some control points first, again: 

close all; clear all; clc
%% 
% We set up some control points (as row vectors): 

%    x  y
p = [1, 1; 
     2, 2; 
     3, 2; 
     3, 3]
%
% Alternatively: 
% p = [0, 0;  3, 0;  3, 2;  2, 2;  2, 3;  3, 3;  4, 4;  5, 3;  6, 2;  6, 1;  6, 0]
%
%% 
% This time, we also need tangents:

%     dx dy
t = [ 0  1;
      1  1;
      1  1; 
     -1  1]/2
%% 
% Let's have a look at them:

figure;
plot (p(:,1), p(:,2), 'ko', 'MarkerFaceColor', 'k'), grid on, axis equal, hold on
axis([min(p(:,1))-1 max(p(:,1))+1 min(p(:,2))-1 max(p(:,2))+1])
xticks(min(p(:,1))-1:0.5:max(p(:,1))+1)
yticks(min(p(:,2))-1:0.5:max(p(:,2))+1)
quiver(p(:,1), p(:,2), t(:,1), t(:,2), 0, 'k', 'LineWidth', 1.5)
%% 
% To get the coefficients of the Hermite splines, we also need the Hermite matrix, 
% $\mathbf{M}_H$: 

M_H = [  2 -2  1  1; ...
        -3  3 -2 -1; ...
         0  0  1  0; ...
         1  0  0  0] % the Hermite matrix
%% 
% With this, we are ready to compute and visualize the interpolating Hermite 
% spline curve:

figure;
cm = [166,206,227; 31,120,180; 178,223,138; 51,160,44; 251,154,153; 227,26,28; 253,191,111; 255,127,0]/256; 
plot (p(:,1), p(:,2), 'ko', 'MarkerFaceColor', 'k'), grid on, axis equal, hold on
axis([min(p(:,1))-1 max(p(:,1))+1 min(p(:,2))-1 max(p(:,2))+1])
xticks(min(p(:,1))-1:0.5:max(p(:,1))+1)
yticks(min(p(:,2))-1:0.5:max(p(:,2))+1)
quiver(p(:,1), p(:,2), t(:,1), t(:,2), 0, 'k', 'LineWidth', 1.5)
FineLine = linspace(0, 1, 17).'; 
for s = 1:(size(p,1)-1)
    x = M_H * [p(s,:); p(s+1,:); t(s,:); t(s+1,:)] % solve for the coefficients per spline curve
    q = x(1,:).*power(FineLine,3) + x(2,:).*power(FineLine,2) + x(3,:).*FineLine + x(4,:); 
    plot(q(:,1), q(:,2), '+', 'Color', cm(2*s+1,:), 'LineWidth', 1.5, 'MarkerSize', 4)
    plot(q(:,1), q(:,2),      'Color', cm(2*s+1,:), 'LineWidth', 1.5)
end
%% 
% Let's get some impression of how the spline curve responds to varying one 
% of the tangents:

ys = (3:-2:-3).'; % let's vary the y-component of the chosen tangent
ts = [ones(length(ys),1) ys]/2; 
t(1,:) = [ 0 1.5]; % let's use also another tangent in the first point
t(4,:) = [-2 0];   % let's use also another tangent in the last point
figure;
plot (p(:,1), p(:,2), 'ko', 'MarkerFaceColor', 'k'), grid on, axis equal, hold on
axis([min(p(:,1))-1 max(p(:,1))+1 min(p(:,2))-1 max(p(:,2))+1])
xticks(min(p(:,1))-1:0.5:max(p(:,1))+1)
yticks(min(p(:,2))-1:0.5:max(p(:,2))+1)
for v = 1:length(ys)
    t(3,:) = ts(v,:); % set in the chosen tangent
    quiver(p(:,1), p(:,2), t(:,1), t(:,2), 0, 'k', 'LineWidth', 1.5)
    for s = 1:(size(p,1)-1)
        x = M_H * [p(s,:); p(s+1,:); t(s,:); t(s+1,:)]; % solve for the coefficients per spline curve
        q = x(1,:).*power(FineLine,3) + x(2,:).*power(FineLine,2) + x(3,:).*FineLine + x(4,:);
        plot(q(:,1), q(:,2), '+', 'Color', cm(2*s+1,:), 'LineWidth', 1.5, 'MarkerSize', 4)
        plot(q(:,1), q(:,2),      'Color', cm(2*s+1,:), 'LineWidth', 1.5)
    end
end
%% 
% EOF.