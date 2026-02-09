#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 09:09:38 2026

@author: nhan.duongtrong@vlu.edu.vn
"""

import numpy as np
import matplotlib.pyplot as plt


file_path_up = '/Users/nhan/Desktop/Si-MoS2-gases/new/1.Si-MoS2/dos/LDOS_ELEMENTS_UP.dat'
file_path_down = '/Users/nhan/Desktop/Si-MoS2-gases/new/1.Si-MoS2/dos/LDOS_ELEMENTS_DW.dat'

def read_and_check_data(file_path):
    try:
        data = np.loadtxt(file_path)
        print(f"Data from {file_path} loaded successfully.")
        if data.ndim == 2 and data.shape[1] >= 4:
            return data
        else:
            print(f"Error: Invalid data structure in {file_path}")
            return None
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

data_up = read_and_check_data(file_path_up)
data_dn = read_and_check_data(file_path_down)

if data_up is not None and data_dn is not None:

    energy = data_up[:, 0] 
    mo_up = data_up[:, 1]
    s_up = data_up[:, 2]
    si_up = data_up[:, 3]
    total_up = mo_up + s_up + si_up 
    
    energy = data_dn[:, 0] 
    mo_dn = data_dn[:, 1]
    s_dn = data_dn[:, 2]
    si_dn = data_dn[:, 3]
    total_dn = mo_dn + s_dn + si_dn
    
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
        'legend.fontsize': 18,
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

    plt.fill_betweenx(energy, 0, total_up, color='gray', alpha=0.5)
    
    plt.plot(total_up, energy, color='gray', linewidth=3, label='Total', zorder=1)
    plt.plot(mo_up, energy, color='blue', linewidth=3,label='Mo', zorder=2)
    plt.plot(s_up, energy, color='green', linewidth=3,label='S', zorder=2)
    plt.plot(si_up, energy, color='orange', linewidth=3,label='Si', zorder=2)
    
    plt.axhline(y=0, color='red', linestyle='--', linewidth=3)  
    plt.ylim(-1.5, 1.5)  
    plt.xlim(0, 60)
    

    plt.xlabel('DOS (States/eV·Unit cell)')
    plt.ylabel('Energy (eV)')


    plt.legend(
        loc='upper right', 
        fontsize=22,
        frameon=True,
        bbox_to_anchor=(1, 0.5),
        handlelength=1.5,
        handletextpad=0.5
    )
    
    plt.grid(False)
    plt.tight_layout()
    plt.show()
else:
    print("Error: Failed to load data files.")
