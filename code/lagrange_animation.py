import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define positions and velocities vs time
def q_accel(a, v0, y0, t):
    """
    Motion with constant acceleration.
    Position vs time.
    """
    return y0 + v0*t + a*np.power(t, 2) / 2

def v_accel(a, v0, t):
    """
    Motion with constant acceleration.
    Velocity vs time.
    """
    return v0 + a*t

# special case -- zero acceleration.
def q_const(v0, y0, t):
    return q_accel(0, v0, y0, t)
def v_const(v0, t):
    return v_accel(0, v0, t)

# mix of two motions: constant velocity and constant acceleration
def q_alpha(alpha, a, v0, v1, y0, t):
    return alpha * q_accel(a, v0, y0, t) + (1-alpha) * q_const(v1, y0, t)

def q_osc(y0, T, t):
    """
    Oscillating from y=y0 to y=0 and up to y=2*y0.
    """
    return y0*(1-np.sin(np.pi*t/2/T))
def v_osc(y0, T, t):
    return -y0*np.pi/2/T*np.cos(np.pi*t/2/T)


def Lagrangian_free(q, v, m):
    """
    Lagrangian of a body free from forces.
    """
    return m*np.power(v, 2)/m

def Lagrangian_force(q, v, m, a):
    """
    Lagrangian of a body under the action of constant force.
    """
    return m*np.power(v, 2)/m - m*a*q

def Lagrangian_osc(q, v, m, T):
    """
    Lagrangian of an oscillator.
    """
    omega = 2*np.pi/T
    return m*np.power(v, 2)/m - m*omega**2*q/2


a = -10  # m/s^2 acceleration
v0 = 0  # free fall with zero velocity
y0 = 1  # m, initial height
m = 1  # kg, mass of the body
T = np.sqrt(2 * y0 / np.abs(a))
v1 = -y0 / T
ts = np.linspace(0, T, 600)

# time-dependent values
q0s = q_alpha(0, a, v0, v1, y0, ts)
q0p5s = q_alpha(0.5, a, v0, v1, y0, ts)
q1s = q_alpha(1, a, v0, v1, y0, ts)
qos = q_osc(y0, T, ts)

# first, show the animation in Newtonian picture
fig, ax = plt.subplots()
# Time evolution
line1 = ax.plot(q0s[0],ts[0], c='r', marker='o', label="alpha=0", alpha=0.4)[0]
line2 = ax.plot(q0p5s[0], ts[0], c='b', marker='o', label="alpha=0.5", alpha=0.4)[0]
line3 = ax.plot(q1s[0], ts[0], c='g', marker='o', label="alpha=1.0", alpha=0.4)[0]
line4 = ax.plot(qos[0], ts[0], c='m', marker='o', label="oscillator", alpha=0.4)[0]

xss = 0 * ts
x1s = 0.1 + xss
x2s = 0.2 + xss
x3s = 0.3 + xss
x4s = 0.4 + xss

all_xss = np.concatenate((x1s, x2s, x3s, x4s))
all_qs = np.concatenate((q0s, q0p5s, q1s, qos))
xmin = all_xss.min() - 0.2
xmax = all_xss.max() + 0.2
ymin = all_qs.min() - 0.1
ymax = all_qs.max()

ax.hlines(0, xmin, xmax)

ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax], ylabel='Y [m]', xlabel='X [m]')
ax.legend(loc="upper right")
ax.set_title("Vertical motion in time")

def update(frame):
    line1.set_xdata(x1s[frame-1:frame])
    line1.set_ydata(q0s[frame-1:frame])

    line2.set_xdata(x2s[frame-1:frame])
    line2.set_ydata(q0p5s[frame-1:frame])

    line3.set_xdata(x3s[frame-1:frame])
    line3.set_ydata(q1s[frame-1:frame])

    line4.set_xdata(x4s[frame-1:frame])
    line4.set_ydata(qos[frame-1:frame])

    return (line1, line2, line3, line4)

num_steps = len(ts)
ani = animation.FuncAnimation(fig=fig, func=update, frames=num_steps, interval=1)
plt.show()
plt.close()


# Second, show anitation in Lagrange picture
fig, ax = plt.subplots()
# Time evolution
line1 = ax.plot(q0s[0],ts[0], c='r',label="alpha=0")[0]
line2 = ax.plot(q0p5s[0], ts[0], c='b',label="alpha=0.5")[0]
line3 = ax.plot(q1s[0], ts[0], c='g',label="alpha=1.0")[0]
line4 = ax.plot(qos[0], ts[0], c='m',label="oscillator")[0]

ymin = ts.min()
ymax = ts.max()
xmin = all_qs.min()
xmax = all_qs.max()

ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax], ylabel='Time [s]', xlabel='Position [m]')
ax.legend(loc="upper right")
ax.set_title("Configuration vs time")

def update(frame):
    line1.set_ydata(ts[:frame])
    line1.set_xdata(q0s[:frame])

    line2.set_ydata(ts[:frame])
    line2.set_xdata(q0p5s[:frame])

    line3.set_ydata(ts[:frame])
    line3.set_xdata(q1s[:frame])

    line4.set_ydata(ts[:frame])
    line4.set_xdata(qos[:frame])

    return (line1, line2, line3, line4)

num_steps = len(ts)
ani = animation.FuncAnimation(fig=fig, func=update, frames=num_steps,
                              interval=1, repeat=False)
plt.show()
plt.close()
fig.savefig("lagrange_vertical.svg")

# Third, show animation of Lagrange functions
fig, ax = plt.subplots()

v0s = v_const(v1, ts)
v1s = v_accel(a, v0, ts)
vos = v_osc(y0, T, ts)

# Free lagrangian for different motions
L_free_q0s = Lagrangian_free(q0s, v0s, m)
L_free_q1s = Lagrangian_free(q1s, v1s, m)
L_free_osc = Lagrangian_free(qos, vos, m)

# Time evolution
line1 = ax.plot(ts[0], L_free_q0s[0], c='r',label="a=0")[0]
line2 = ax.plot(ts[0], L_free_q1s[0], c='b',label="a=const")[0]
line3 = ax.plot(ts[0], L_free_osc[0], c='g',label="oscillate")[0]

all_Ls = np.concatenate((L_free_q0s, L_free_q1s, L_free_osc))

ymin = all_Ls.min()
ymax = all_Ls.max()
xmin = ts.min()
xmax = ts.max()

ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax], xlabel='Time [s]', ylabel='Lagrangian [J*s]')
ax.legend(loc="upper right")
ax.set_title("Lagrangian of free particle vs time")

def update(frame):
    line1.set_xdata(ts[:frame])
    line1.set_ydata(L_free_q0s[:frame])

    line2.set_xdata(ts[:frame])
    line2.set_ydata(L_free_q1s[:frame])

    line3.set_xdata(ts[:frame])
    line3.set_ydata(L_free_osc[:frame])

    return (line1, line2, line3)

num_steps = len(ts)
ani = animation.FuncAnimation(fig=fig, func=update, frames=num_steps, interval=1)
plt.show()
plt.close()
