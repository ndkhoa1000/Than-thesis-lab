#!/bin/bash
#SBATCH --job-name=vasp_job
#SBATCH --nodes=1              # Number of nodes
#SBATCH --ntasks=4             # Number of tasks (cores)
#SBATCH --mem=8000             # Memory in MB (adjust to your system)
#SBATCH --time=24:00:00        # Max runtime (24 hours)
#SBATCH --output=vasp_%j.out   # Output file (%j = job ID)
#SBATCH --error=vasp_%j.err    # Error file
#SBATCH --partition=ctu
module load oneapi/2024.2
module load vasp/6.5.0
echo "Program started at $date"
mpirun -np $SLURM_NTASKS vasp_gam

