#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 09:09:38 2026

@author: nhan.duongtrong@vlu.edu.vn
"""
import numpy as np
import matplotlib.pyplot as plt


file_up = 'PBAND_ELEMENT_UP.dat'
file_down = 'PBAND_ELEMENT_DW.dat'

def load_b_data(file_path):
    data = np.loadtxt(file_path)
    return data[:, 0], data[:, 1], data[:, 4]

plt.rcParams.update({
   # Font settings
    'font.family': 'serif',
    'font.serif': 'Times New Roman',
    'font.size': 15,
    'font.weight': 'bold',
    
    # Axes settings
    'axes.labelsize': 40,
    'axes.titlesize': 1,
    'axes.linewidth': 5,
    
    # Tick settings
    'xtick.labelsize': 35,
    'ytick.labelsize': 35,
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    
    # Legend settings
    'legend.fontsize': 12,
    'legend.frameon': True,
    
    # Line settings
    'lines.linewidth': 3,
    'lines.markersize': 8,
    
    # Grid settings
    'grid.linewidth': 0.8,
    'grid.alpha': 0.3,
    
    # Figure settings
    'figure.figsize': (10, 12),
    'savefig.dpi': 600,
    'savefig.bbox': 'tight'
})

k_up, e_up, si_up = load_b_data(file_up)
k_down, e_down, si_down = load_b_data(file_down)



plt.plot(k_up, e_up, 
         color='navy', 
         linewidth=2, 
         alpha=0.8, 
         zorder=1,
         )
plt.scatter(k_up, e_up,
            s=si_up*800,  
            c='#00ff00',  
            alpha=0.9,
            edgecolors='green', 
            linewidth=0.8,
            marker='o',
            label='Si',
            zorder=3)

high_sym_points = [0, 0.230, 0.362, 0.627]
for x in high_sym_points:
    plt.axvline(x, color='gray', linestyle='--', linewidth=3, alpha=0.9, zorder=2)


plt.xlim(0, 0.627)
plt.ylim(-1.5, 1.5)


plt.axhline(0, color='red', linestyle='--', linewidth=3.0, alpha=0.9)

plt.xticks(high_sym_points, ['Γ', 'M', 'K', 'Γ'], 
          )
plt.yticks( )
plt.ylabel('Energy (eV)')
plt.xlabel('K-path')




plt.tight_layout()
plt.show()
