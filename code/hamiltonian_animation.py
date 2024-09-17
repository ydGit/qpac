"""
This script illustrates the motion of an oscillator from
different perspectives (representations).
First it shows how position and momentum change in time.
Next, it shows how the state xi=(x,p) changes in time by
plotting it as a point moving in *phase space*.

Oscillator is used here is a body of mass m attached
to a spring of spring constant k.

Initial state of the oscillator xi0=(x0, p0) is specified by
initial position x0 and initial momentum p0.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def xi_osc(xi0, k, m, t):
    """
    Calculate state (position and momentum) of the oscillator
    given initial state xi0=(x0,p0), parameters of the oscillator
    such as mass and spring constant, and time
    """
    x0, p0 = xi0
    H = p0*p0/2/m + k*x0*x0/2  # energy
    xm = np.sqrt(2*H/k)  # max stretch
    pm = np.sqrt(2*H*m)  # max momentum
    omega = np.sqrt(k/m)
    phase = omega*t

    x = x0*np.cos(phase) + xm/pm*p0*np.sin(phase)
    p = p0*np.cos(phase) - pm/xm*x0*np.sin(phase)

    xi = (x,p)

    return xi

# Oscillator parameters:
k = 10.0  # N/m
m = 0.2  # kg

interval = 5# 0.3  # time between animation frames
# Let's study several different states at once
number_of_particles = 30 # group of initial conditions
x0_avg = 0.1  # m, average position
v0_avg = 0.5  # m/s, average velocity
x_spread = 0.1
v_spread = 0.1
delta_x0 = x_spread*np.abs(x0_avg)  # 30% variation
delta_v0 = v_spread*np.abs(v0_avg)  # 30% variation
# Generate random positions and velocities
x0s = np.random.normal(loc=x0_avg, scale=delta_x0, size=number_of_particles)
v0s = np.random.normal(loc=v0_avg, scale=delta_v0, size=number_of_particles)
p0s = m*v0s

omega = np.sqrt(k/m)  # oscillation frequency
T = 2*np.pi/omega  # period of a single oscillation
ts = np.linspace(0, T, 600)

# time-dependent values
xi0s = []
xis = []
for i in range(number_of_particles):
    x0 = x0s[i]
    p0 = p0s[i]
    xi0 = (x0, p0)
    xi = xi_osc(xi0, k, m, ts)
    xi0s.append(xi0)
    xis.append(xi)

# from pdb import set_trace
# set_trace()

# first, show the animation in Newtonian picture
fig, ax = plt.subplots()
# Time evolution
lines = []
for i in range(number_of_particles):
    xi = xis[i]  # state of i-th *variant*
    xs = xi[0]
    ps = xi[1]
    line = ax.plot(xs[0], ts[0], c='r', marker='.', label="oscillator", alpha=0.4)[0]
    lines.append(line)

xmax = ts.max()
xmin = ts.min()
ymax = 0
ymin = 0
for i in range(number_of_particles):
    xi = xis[i]  # state of i-th *variant*
    xs = xi[0]
    if xs.max() > ymax:
        ymax = xs.max()
    if xs.min() < ymin:
        ymin = xs.min()
expand_factor = 1.1
xmax *= expand_factor
xmin *= expand_factor
ymin *= expand_factor
ymax *= expand_factor


ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax], ylabel='X [m]', xlabel='T [s]')
# ax.legend(loc="upper right")
ax.set_title("Oscillator position in time")

def update(frame):
    for i in range(number_of_particles):
        line = lines[i]
        xi = xis[i]  # state of i-th *variant*
        xs = xi[0]
        line.set_xdata(ts[frame-1:frame])
        line.set_ydata(xs[frame-1:frame])

    return lines

num_steps = len(ts)
ani = animation.FuncAnimation(fig=fig, func=update, frames=num_steps, interval=interval)
plt.show()
plt.close()


# Second, show motion in phase space
fig, ax = plt.subplots()
# Time evolution
lines = []
for i in range(number_of_particles):
    xi = xis[i]  # state of i-th *variant*
    xs = xi[0]
    ps = xi[1]
    line = ax.plot(xs[0], ps[0], c='b', marker='.', label="oscillator", alpha=0.4)[0]
    lines.append(line)

xmax = 0
xmin = 0
pmax = 0
pmin = 0
for i in range(number_of_particles):
    xi = xis[i]  # state of i-th *variant*
    xs = xi[0]
    ps = xi[1]
    if xs.max() > xmax:
        xmax = xs.max()
    if xs.min() < xmin:
        xmin = xs.min()
    if ps.max() > pmax:
        pmax = ps.max()
    if ps.min() < pmin:
        pmin = ps.min()
expand_factor = 1.1
xmax *= expand_factor
xmin *= expand_factor
pmin *= expand_factor
pmax *= expand_factor

ax.set(xlim=[xmin, xmax], ylim=[pmin, pmax], xlabel='X [m]', ylabel='P [kg*m/s]')
# ax.legend(loc="upper right")
ax.set_title("Oscillator Phase Space")

def update(frame):
    for i in range(number_of_particles):
        line = lines[i]
        xi = xis[i]  # state of i-th *variant*
        xs = xi[0]
        ps = xi[1]
        line.set_xdata(xs[frame-1:frame])
        line.set_ydata(ps[frame-1:frame])

    return lines

num_steps = len(ts)
ani = animation.FuncAnimation(fig=fig, func=update, frames=num_steps, interval=interval)
plt.show()
plt.close()
