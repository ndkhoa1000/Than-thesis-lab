#!/bin/bash
#SBATCH --job-name=vasp_relax
#SBATCH --partition=ctu
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --time=24:00:00
#SBATCH --mem=0
#SBATCH --output=vasp_%j.out
#SBATCH --error=vasp_%j.err

module purge
module load vasp/6.5.0

# tránh oversubscribe
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
ulimit -s unlimited

# Intel MPI: tránh shm:tcp (dễ treo) -> dùng shm:ofi
export I_MPI_FABRICS=shm:ofi
export FI_PROVIDER=tcp
export I_MPI_OFI_PROVIDER=tcp

echo "Start: $(date)"
echo "Workdir: $(pwd)"
echo "NTASKS=$SLURM_NTASKS"

mpirun -np $SLURM_NTASKS vasp_std

echo "End: $(date)"