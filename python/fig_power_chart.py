import matplotlib.pyplot as plt
import numpy as np

# Khớp bề rộng \textwidth khổ A4 (~6.3 in) để giữ đúng cỡ chữ >= 12 pt khi chèn 1:1
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 12

modes = ['Mode 1\n(Front)', 'Mode 2\n(Front+RGB)']
currents = [60, 140]            # mA (Table 4.1)
runtimes = [4000/60, 4000/140]  # Thời lượng lý thuyết (4000 mAh / I)

colors_curr = ['#2563EB', '#DC2626']  # Xanh dương, Đỏ
colors_time = ['#059669', '#D97706']  # Xanh lá, Cam

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 3.8), dpi=300)
fig.suptitle('Steady Lighting Modes: Power & Ideal Runtime',
             fontsize=13, fontweight='bold', color='#0F172A', y=0.87)

x = np.arange(len(modes))
bar_w = 0.52

# --- (a) Dòng tiêu thụ ---
bars1 = ax1.bar(x, currents, width=bar_w, color=colors_curr, edgecolor='#1E293B', linewidth=1.0, zorder=3)
ax1.set_title('(a) Current Draw', fontsize=12, fontweight='bold', color='#0F172A', pad=8)
ax1.set_ylabel('Current (mA)', fontsize=12, color='#0F172A')
ax1.set_xticks(x)
ax1.set_xticklabels(modes, fontsize=12)
ax1.set_ylim(0, 185)
ax1.grid(axis='y', linestyle='--', alpha=0.5, zorder=0)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

for bar, val in zip(bars1, currents):
    ax1.text(bar.get_x() + bar.get_width()/2, val + 5, f'~{val} mA',
             ha='center', va='bottom', fontsize=12, fontweight='bold', color='#0F172A')

ax1.annotate('~2.3×', xy=(0.73, 140), xytext=(0.15, 132),
             ha='center', va='center', fontsize=12, fontweight='bold', color='#DC2626',
             arrowprops=dict(arrowstyle='->', color='#DC2626', lw=1.5, connectionstyle='arc3,rad=-0.2'))

# --- (b) Thời lượng pin lý thuyết ---
bars2 = ax2.bar(x, runtimes, width=bar_w, color=colors_time, edgecolor='#1E293B', linewidth=1.0, zorder=3)
ax2.set_title('(b) Ideal Runtime*', fontsize=12, fontweight='bold', color='#0F172A', pad=8)
ax2.set_ylabel('Time (hours)', fontsize=12, color='#0F172A')
ax2.set_xticks(x)
ax2.set_xticklabels(modes, fontsize=12)
ax2.set_ylim(0, 88)
ax2.grid(axis='y', linestyle='--', alpha=0.5, zorder=0)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

for bar, val in zip(bars2, runtimes):
    ax2.text(bar.get_x() + bar.get_width()/2, val + 2.5, f'{val:.1f} h',
             ha='center', va='bottom', fontsize=12, fontweight='bold', color='#0F172A')

fig.text(0.5, -0.05, '*Ideal estimate: 4000 mAh / I (excludes losses).',
         ha='center', va='bottom', fontsize=12, style='italic', color='#475569')

plt.tight_layout(rect=[0, 0, 1, 0.90])
plt.savefig('power_barchart.pdf', bbox_inches='tight', facecolor='white')