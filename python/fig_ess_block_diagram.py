import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Exact LaTeX A4 \textwidth (~6.3 inches) so 1:1 scaling preserves true 12pt+ fonts
plt.rcParams['font.family'] = 'DejaVu Sans'
fig, ax = plt.subplots(figsize=(6.3, 9.1), dpi=300)
ax.set_xlim(0, 6.3)
ax.set_ylim(0, 9.1)
ax.axis('off')

def draw_box(x, y, w, h, title, subtitle="", facecolor="#FFFFFF", edgecolor="#334155", title_color="#0F172A", lw=1.3):
    box = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.04,rounding_size=0.10",
        facecolor=facecolor, edgecolor=edgecolor, linewidth=lw, zorder=3
    )
    ax.add_patch(box)
    if subtitle:
        ax.text(x + w/2, y + h*0.68, title, ha='center', va='center',
                fontsize=12, fontweight='bold', color=title_color, zorder=4)
        ax.text(x + w/2, y + h*0.28, subtitle, ha='center', va='center',
                fontsize=12, color="#334155", zorder=4, linespacing=1.15)
    else:
        ax.text(x + w/2, y + h/2, title, ha='center', va='center',
                fontsize=12, fontweight='bold', color=title_color, zorder=4)

def draw_group(x, y, w, h, label, facecolor, edgecolor, label_color):
    group = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.04,rounding_size=0.12",
        facecolor=facecolor, edgecolor=edgecolor, linewidth=1.2, linestyle='--', zorder=1
    )
    ax.add_patch(group)
    ax.text(x + 0.12, y + h - 0.12, label, ha='left', va='top',
            fontsize=12, fontweight='bold', color=label_color, zorder=2)

def draw_arrow(x1, y1, x2, y2, color="#1E293B", style="-|>", ls="-", lw=1.6, label="", lx=None, ly=None):
    arrow = patches.FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle=style, mutation_scale=13,
        color=color, linewidth=lw, linestyle=ls, zorder=5
    )
    ax.add_patch(arrow)
    if label:
        tx = (x1 + x2)/2 if lx is None else lx
        ty = (y1 + y2)/2 if ly is None else ly
        ax.text(tx, ty, label, ha='center', va='center', fontsize=12,
                color=color, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.10", facecolor="white", edgecolor="none", alpha=0.92),
                zorder=6)

# Title (14pt)
ax.text(3.15, 8.88, "E-ShoeS (ESS) System Architecture", ha='center', va='center',
        fontsize=14, fontweight='bold', color="#0F172A")

# --- 1. ENERGY HARVESTING & POWER (TOP, 2x2 grid) ---
draw_group(0.12, 6.05, 6.06, 2.55, "1. Energy Harvesting & Power",
           facecolor="#FEFCE8", edgecolor="#CA8A04", label_color="#854D0E")

draw_box(0.28, 7.35, 2.60, 0.80, "PolyK PVDF Film", ">100 V AC Steps", "#FFFFFF", "#CA8A04")
draw_box(3.42, 7.35, 2.60, 0.80, "Rectifier & PMIC", "AEM30940", "#FFFFFF", "#CA8A04")
draw_box(3.42, 6.22, 2.60, 0.80, "Li-Po Battery", "3.7 V, 4000 mAh", "#FEF9C3", "#A16207", lw=1.7)
draw_box(0.28, 6.22, 2.60, 0.80, "DC-DC Regulator", "TPS63031 (3.3 V)", "#FFFFFF", "#CA8A04")

draw_arrow(2.93, 7.75, 3.37, 7.75, "#B45309")
draw_arrow(4.72, 7.30, 4.72, 7.07, "#B45309")
draw_arrow(3.37, 6.62, 2.93, 6.62, "#B45309")

# --- 2. CONTROL & SOS (MIDDLE-LEFT) ---
draw_group(0.12, 2.38, 2.95, 3.22, "2. Control & SOS",
           facecolor="#EFF6FF", edgecolor="#2563EB", label_color="#1E40AF")

draw_box(0.28, 4.50, 2.63, 0.66, "IP67 Button", "Short / Hold 3s", "#FFFFFF", "#2563EB")
draw_box(0.28, 3.50, 2.63, 0.66, "XIAO ESP32-C3", "Lighting MCU", "#DBEAFE", "#1D4ED8")
draw_box(0.28, 2.50, 2.63, 0.66, "MDBT42Q (BLE)", "nRF52832 SOS", "#DBEAFE", "#1D4ED8")

draw_arrow(1.59, 4.45, 1.59, 4.21, "#1D4ED8")
draw_arrow(1.59, 3.45, 1.59, 3.21, "#1D4ED8", style="<->")

# --- 3. LIGHTING & SIGNALING (MIDDLE-RIGHT) ---
draw_group(3.30, 3.45, 2.88, 2.15, "3. Lighting",
           facecolor="#F0FDF4", edgecolor="#16A34A", label_color="#166534")

draw_box(3.46, 4.50, 2.56, 0.66, "Front LEDs", "2x SMD 5730", "#FFFFFF", "#16A34A")
draw_box(3.46, 3.58, 2.56, 0.66, "RGB Strip", "WS2812B (3.7 V)", "#FFFFFF", "#16A34A")

draw_arrow(2.96, 3.96, 3.41, 4.78, "#15803D")
draw_arrow(2.96, 3.78, 3.41, 3.90, "#15803D")

# --- 4. SMARTPHONE APP & AI (BOTTOM) ---
draw_group(0.12, 0.62, 6.06, 1.30, "4. Smartphone Companion App & AI",
           facecolor="#FAF5FF", edgecolor="#9333EA", label_color="#6B21A8")

draw_box(0.28, 0.76, 2.60, 0.72, "AI Smart GPS", "Filter & Save Batt", "#F3E8FF", "#7E22CE")
draw_box(3.42, 0.76, 2.60, 0.72, "SOS Alert", "Send Live Location", "#FEE2E2", "#DC2626", title_color="#991B1B")

draw_arrow(1.59, 2.34, 1.59, 1.97, "#7E22CE", ls="--", lw=1.8, label="BLE", lx=2.12, ly=2.15)
draw_arrow(2.93, 1.12, 3.37, 1.12, "#DC2626")

# --- POWER DISTRIBUTION ---
draw_arrow(1.59, 6.01, 1.59, 5.64, "#EA580C", label="3.3 V", lx=1.08, ly=5.82)
draw_arrow(4.72, 6.01, 4.72, 5.64, "#DC2626", label="3.7 V", lx=5.24, ly=5.82)

# --- LEGEND (12pt) ---
ly = 0.24
ax.plot([0.18, 0.55], [ly, ly], color="#EA580C", lw=2.0)
ax.text(0.62, ly, "3.3V", va='center', fontsize=12, color="#334155")

ax.plot([1.45, 1.82], [ly, ly], color="#DC2626", lw=2.0)
ax.text(1.89, ly, "3.7V", va='center', fontsize=12, color="#334155")

ax.plot([2.72, 3.09], [ly, ly], color="#15803D", lw=2.0)
ax.text(3.16, ly, "Signal", va='center', fontsize=12, color="#334155")

ax.plot([4.35, 4.72], [ly, ly], color="#7E22CE", lw=2.0, ls='--')
ax.text(4.79, ly, "BLE", va='center', fontsize=12, color="#334155")

plt.tight_layout(pad=0.15)
plt.savefig("ess_block_diagram.pdf", bbox_inches='tight', facecolor='white')