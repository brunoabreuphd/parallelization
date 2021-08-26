###
# File: openmp_scaling.py
# Description: 
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Thursday, 26th August 2021, 11:25:02 am
# Last Modified: Thursday, 26th August 2021, 11:28:59 am
#  
# Copyright (c) 2021, Bruno R. de Abreu, National Center for Supercomputing Applications.
# All rights reserved.
# License: This program and the accompanying materials are made available to any individual
#          under the citation condition that follows: On the event that the software is
#          used to generate data that is used implicitly or explicitly for research
#          purposes, proper acknowledgment must be provided in the citations section of
#          publications. This includes both the author's name and the National Center
#          for Supercomputing Applications. If you are uncertain about how to do
#          so, please check this page: https://github.com/babreu-ncsa/cite-me.
#          This software cannot be used for commercial purposes in any way whatsoever.
#          Omitting this license when redistributing the code is strongly disencouraged.
#          The software is provided without warranty of any kind. In no event shall the
#          author or copyright holders be liable for any kind of claim in connection to
#          the software and its usage.
###
import os
import subprocess
import matplotlib.pyplot as plt
import sys

# set environment (gfortran here)
# If you start this notebook from a conda env, sometimes your PATH variable will not include everything that is under your user-defined environment (it may not load your ~/.bashrc). 
# In my case, I ran this notebook in a Mac where GCC was installed via Homebrew. Therefore, I had to do:
# os.environ['PATH'] = os.environ['PATH'] + ':/opt/homebrew/bin'
# for this to work properly. On a shared environment this is less likely to happen, but you may need to do a 'module load gcc'
os.environ['PATH'] = os.environ['PATH'] + ':/opt/homebrew/bin'
try:
    comp = subprocess.run(['gfortran', '--version'])
    print('gfortran is available')
except:
    print('gfortran could not be found. Make sure your PATH is set up correctly.')
    sys.exit()

# define compiler name, OpenMP flag and source file name
compiler = 'gfortran'
flag = '-fopenmp'
sourcefile = 'matmul_openmp.f90'

def retrieve_time(stdout):
    """
    Retrieves time from subprocesses.run.stdout (specific to this code)
    You may have to adjust this depending on the standard Fortran format output of your machine.
    """
    x = str(stdout)
    x = x.replace("s", "")
    x = x.replace("\\n", "")
    x = x.replace("b", "")
    x = x.replace("'", "")
    return float(x[-25:-8])

# Compile code
comp = subprocess.run([compiler, flag, sourcefile], capture_output=True)
if comp.returncode != 0:
    print('Compilation failed!')
    print('Error message: ', comp.stderr)
    sys.exit()
else:
    print('Compiled!')

# Run code with different number of threads
nthreads = 1
n = []
t = []
for i in range(6):
    os.environ['OMP_NUM_THREADS']=str(nthreads)
    run = subprocess.run(['./a.out'], capture_output=True)
    print("Number of threads: ", nthreads, run.stdout)
    t.append(retrieve_time(run.stdout))
    n.append(nthreads)
    nthreads = nthreads*2

# Plot results
scaling = [t[0] / tN for tN in t]

plt.figure()
plt.scatter(n, scaling)
plt.xscale('log')
plt.xlabel('$N$ (# of threads)',fontsize=18)
plt.ylabel('$t_1 / t_N$', fontsize=20)
plt.xticks(fontsize=16);
plt.yticks(fontsize=16);
plt.title('OpenMP scaling', fontsize=16);
plt.savefig('openmp_scaling.png', bbox_inches='tight')