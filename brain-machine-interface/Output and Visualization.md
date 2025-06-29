绘制单个神经元的电压、脉冲随着时间的变化情况。示例代码：
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# 设置随机种子以确保结果可重现
np.random.seed(42)

# 创建模拟数据
def simulate_neuron(duration=1000, dt=0.1, baseline=-70, threshold=-55, spike_peak=40):
    """
    模拟神经元电压和脉冲活动
    参数:
        duration: 模拟总时长(ms)
        dt: 时间步长(ms)
        baseline: 静息电位(mV)
        threshold: 动作电位阈值(mV)
        spike_peak: 动作电位峰值(mV)
    返回:
        t: 时间数组
        voltage: 电压数组
        spike_times: 动作电位发生时间数组
    """
    n_steps = int(duration / dt)
    t = np.arange(0, duration, dt)
    voltage = baseline * np.ones(n_steps)
    
    # 添加背景噪声
    noise = np.random.normal(0, 0.5, n_steps)
    voltage += noise
    
    # 添加输入电流模拟突触输入
    input_current = np.zeros(n_steps)
    for start in range(100, duration, 200):
        end = min(start + 50, duration)
        input_current[int(start/dt):int(end/dt)] = 15
    
    # 模拟神经元响应
    spike_times = []
    refractory = 0
    
    for i in range(1, n_steps):
        # 模拟膜电位动态
        dv = 0.1 * (input_current[i] - (voltage[i-1] - baseline)) * dt
        voltage[i] += dv
        
        # 不应期处理
        if refractory > 0:
            voltage[i] = baseline - 10  # 超极化
            refractory -= dt
            continue
        
        # 检查是否达到阈值并产生动作电位
        if voltage[i] > threshold:
            # 记录动作电位时间
            spike_times.append(t[i])
            # 模拟动作电位波形
            voltage[i] = spike_peak
            if i < n_steps - 1:
                voltage[i+1] = baseline - 15  # 后超极化
            # 设置不应期
            refractory = 2  # ms
    
    return t, voltage, np.array(spike_times)

# 生成模拟数据
duration = 500  # 模拟时长(毫秒)
t, voltage, spike_times = simulate_neuron(duration=duration)

# 创建绘图布局
fig = plt.figure(figsize=(12, 8), dpi=100)
gs = GridSpec(3, 1, height_ratios=[3, 1, 1])

# 绘制电压随时间变化图
ax1 = fig.add_subplot(gs[0])
ax1.plot(t, voltage, 'b-', linewidth=1.5)
ax1.set_title('神经元膜电位随时间变化', fontsize=14, fontweight='bold')
ax1.set_ylabel('电压 (mV)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.axhline(y=-55, color='r', linestyle='--', alpha=0.7, label='阈值')
ax1.axhline(y=-70, color='g', linestyle='--', alpha=0.7, label='静息电位')
ax1.legend(loc='upper right')

# 在电压图上标记动作电位
if len(spike_times) > 0:
    spike_indices = np.searchsorted(t, spike_times)
    ax1.plot(spike_times, voltage[spike_indices], 'ro', markersize=6, label='动作电位')
    ax1.legend(loc='upper right')

# 绘制脉冲栅格图
ax2 = fig.add_subplot(gs[1], sharex=ax1)
if len(spike_times) > 0:
    ax2.vlines(spike_times, 0, 1, color='k', linewidth=1.5)
ax2.set_title('脉冲栅格图 (动作电位时间点)', fontsize=14, fontweight='bold')
ax2.set_yticks([0])
ax2.set_yticklabels([''])
ax2.set_ylabel('脉冲', fontsize=12)
ax2.set_ylim(-0.1, 1.1)
ax2.grid(True, axis='x', linestyle='--', alpha=0.7)

# 绘制输入电流
ax3 = fig.add_subplot(gs[2], sharex=ax1)
input_current = np.zeros_like(t)
for start in range(100, duration, 200):
    end = min(start + 50, duration)
    input_current[(t >= start) & (t <= end)] = 15
ax3.plot(t, input_current, 'g-', linewidth=2)
ax3.set_title('输入电流', fontsize=14, fontweight='bold')
ax3.set_xlabel('时间 (ms)', fontsize=12)
ax3.set_ylabel('电流 (pA)', fontsize=12)
ax3.grid(True, linestyle='--', alpha=0.7)
ax3.set_ylim(-1, 20)

plt.tight_layout()
plt.show()
```