import matplotlib.pyplot as plt
import numpy as np



def if_model(tau_v, R, v_th, t_step, v_t, I):
    v = np.zeros(100)
    for i in range(100): # simulate for 100 ms
        if v_t > v_th: # reset v_t if it exceeds threshold  
            v_t = 0 
            
        v_t = v_t + t_step/tau_v * (-v_t + R*I)
        v[i] = v_t
    return v

if __name__ == "__main__": 
    tau_v = 10
    R = 1
    v_th = 10
    t_step = 1 # 1ms
    v_t = 0
    
    v_9 = if_model(tau_v, R, v_th, t_step, v_t, 9)
    v_11 = if_model(tau_v, R, v_th, t_step, v_t, 11)
    v_15 = if_model(tau_v, R, v_th, t_step, v_t, 15)
    
    plt.subplot(1,3,1)    
    plt.plot(np.arange(100), v_9)
    plt.title('I = 9')
    
    plt.subplot(1,3,2)  
    plt.plot(np.arange(100), v_11)
    plt.title('I = 11')
    
    plt.subplot(1,3,3)
    plt.plot(np.arange(100), v_15)
    plt.title('I = 15')
    
    plt.show()