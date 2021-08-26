import os
import subprocess
import matplotlib.pyplot as plt
import sys

# set environment (gcc here)
# If you start this notebook from a conda env, sometimes your PATH variable will not include everything that is under your user-defined environment (it may not load your ~/.bashrc). 
# In my case, I ran this notebook in a Mac where GCC was installed via Homebrew. Therefore, I had to do:
# os.environ['PATH'] = os.environ['PATH'] + ':/opt/homebrew/bin'
# for this to work properly. On a shared environment this is less likely to happen, but you may need to do a 'module load gcc'
try:
    comp = subprocess.run(['gcc', '--version'])
    print('gcc is available')
except:
    print('gcc could not be found. Make sure your PATH is set up correctly.')
    sys.exit()

# define compiler name, OpenMP flag and source file name
compiler = 'gcc'
flag = '-fopenmp'
sourcefile = 'saxpy_openmp.c'

def retrieve_time(stdout):
    """
    Retrieves time from subprocesses.run.stdout (specific to this code)
    You may have to adjust this depending on the standard C format output of your machine.
    """
    x = str(stdout)
    x = x.replace("s", "")
    x = x.replace("\n", "")
    x = x.replace("b", "")
    x = x.replace("'", "")
    return float(x[-10:-2])

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

