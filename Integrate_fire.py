import matplotlib.pyplot as plt

tau_v = 10
R = 1
v_th = 10
t_step = 1 # 1ms
v_t = 0

for i in range(100): # simulate for 100 ms
    v_t = v_t + t_step/tau_v * (-v_t + R*)