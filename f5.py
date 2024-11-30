# ----------------------------------------------------
# 振幅変調とその復調，位相変調とその復調を確認するコード
# ----------------------------------------------------
# 2024-11-30 福田
# ----------------------------------------------------

import math
import matplotlib.pyplot as plt
import random as rnd

SAMPLE_SIZE = 2000
DATA_SIZE = 10
FILTER_SIZE = 50

# 変数準備 すべてリスト
time = []                       # 時刻
carrier = []                    # キャリア
data = []                       # データ
data_mod = []                   #############################################
amp_modulated = []              # 振幅変調信号
amp_demodulated = []            # 振幅変調信号を復号した信号
amp_demodulated_filtered = []   # さらにフィルタ処理した信号

phase_modulated = []            # 位相変調信号
phase_demodulated = []          # 位相変調信号を復号した信号
phase_demodulated_filtered = [] # さらにフィルタ処理した信号

# データの生成
for i in range(DATA_SIZE):
    if(rnd.uniform(0,1)<0.5):
        data.append(0)
    else:
        data.append(1)

# 変調信号の生成
for j in range(DATA_SIZE):
    for i in range(int(SAMPLE_SIZE/DATA_SIZE)):
            amp_modulated.append(0.5*data[j]*math.sin(math.pi*i/50)+0.5*math.sin(math.pi*i/50))
            phase_modulated.append(math.sin(math.pi*i/50 + (1-data[j])*math.pi))
            data_mod.append(data[j])

print(len(amp_modulated))
print(len(phase_modulated))

# 時刻とキャリア
for i in range(SAMPLE_SIZE):
    time.append(i/50*math.pi)
    carrier.append(math.sin(math.pi*i/50))

print(len(time))
print(len(carrier))

# 復調　変調信号にキャリアを掛けるだけ
for i in range(SAMPLE_SIZE):
    amp_demodulated.append(carrier[i]*amp_modulated[i])
    # phase_demodulated.append((carrier[i]*phase_modulated[i]+1)/2)
    phase_demodulated.append(carrier[i]*phase_modulated[i])
    amp_demodulated_filtered.append(0)
    phase_demodulated_filtered.append(0)

# 移動平均フィルタ (ローパスフィルタ)
# フィルタ次数は FILTER_SIZE で指定
for i in range(0,SAMPLE_SIZE-FILTER_SIZE):
    for j in range(0,FILTER_SIZE):
        amp_demodulated_filtered[i] += amp_demodulated[i+j]
        phase_demodulated_filtered[i] += phase_demodulated[i+j]
    amp_demodulated_filtered[i] /= FILTER_SIZE
    phase_demodulated_filtered[i] /= FILTER_SIZE

# -----------------------------------------------
# グラフ準備 
# -----------------------------------------------
# データ        キャリア
# 振幅変調      振幅復調        振幅復調フィルタ後
# 位相変調      位相復調        位相復調フィルタ後
# -----------------------------------------------

fig = plt.figure()
g_data = fig.add_subplot(3,3,1)
g_carrier = fig.add_subplot(3,3,2)
g_amp_modulated = fig.add_subplot(3,3,4)
g_amp_demodulated = fig.add_subplot(3,3,5)
g_amp_demodulated_filtered = fig.add_subplot(3,3,6)
g_phase_modulated = fig.add_subplot(3,3,7)
g_phase_demodulated = fig.add_subplot(3,3,8)
g_phase_demodulated_filtered = fig.add_subplot(3,3,9)

# g_data.plot(time, data)
g_data.plot(time, data_mod)
# g_data.plot(data)
g_carrier.scatter(time, carrier, s=1)
g_amp_modulated.scatter(time, amp_modulated, s=1)
g_amp_demodulated.scatter(time, amp_demodulated, s=1)
g_amp_demodulated_filtered.scatter(time, amp_demodulated_filtered, s=1)
g_phase_modulated.scatter(time, phase_modulated, s=1)
g_phase_demodulated.scatter(time, phase_demodulated, s=1)
g_phase_demodulated_filtered.scatter(time, phase_demodulated_filtered, s=1)

plt.show()

# データの書き出し
for i in range(SAMPLE_SIZE):
    # print(time[i], carrier[i], amp_modulated[i], amp_demodulated[i], phase_modulated[i], phase_demodulated[i], sep=",")
    print(time[i], data_mod[i], carrier[i], amp_modulated[i], amp_demodulated[i], phase_modulated[i], phase_demodulated[i], sep=",")
