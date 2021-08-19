import os
import subprocess
import matplotlib.pyplot as plt
import sys


# set environment (gfortran here)
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


# define compiler name and source file name
compiler = 'gcc'
sourcefile = 'saxpy.c'


def retrieve_time(stdout):
    """
    Retrieves time from subprocesses.run.stdout (specific to this code)
    You may have to adjust this depending on the standard Fortran format output of your machine.
    """
    x = str(stdout)
    x = x.replace("s", "")
    x = x.replace("\n", "")
    x = x.replace("b", "")
    x = x.replace("'", "")
    return float(x[-10:-2])

# list of flags from GCC documentation
o1flags="-fauto-inc-dec -fbranch-count-reg -fcombine-stack-adjustments -fcompare-elim -fcprop-registers -fdce -fdefer-pop -fdelayed-branch -fdse -fforward-propagate -fguess-branch-probability -fif-conversion -fif-conversion2 -finline-functions-called-once -fipa-profile -fipa-pure-const -fipa-reference -fipa-reference-addressable -fmerge-constants -fmove-loop-invariants -fomit-frame-pointer -freorder-blocks -fshrink-wrap -fshrink-wrap-separate -fsplit-wide-types -fssa-backprop -fssa-phiopt -ftree-bit-ccp -ftree-ccp -ftree-ch -ftree-coalesce-vars -ftree-copy-prop -ftree-dce -ftree-dominator-opts -ftree-dse -ftree-forwprop -ftree-fre -ftree-phiprop -ftree-pta -ftree-scev-cprop -ftree-sink -ftree-slsr -ftree-sra -ftree-ter -funit-at-a-time"
o1flags_list = o1flags.split(" ")

o2flags="-falign-functions -falign-jumps -falign-labels -falign-loops -fcaller-saves -fcode-hoisting -fcrossjumping -fcse-follow-jumps -fcse-skip-blocks -fdelete-null-pointer-checks -fdevirtualize -fdevirtualize-speculatively -fexpensive-optimizations -ffinite-loops -fgcse -fgcse-lm -fhoist-adjacent-loads -finline-functions -finline-small-functions -findirect-inlining -fipa-bit-cp -fipa-cp -fipa-icf -fipa-ra -fipa-sra -fipa-vrp -fisolate-erroneous-paths-dereference -flra-remat -foptimize-sibling-calls -foptimize-strlen -fpartial-inlining -fpeephole2 -freorder-blocks-algorithm=stc -freorder-blocks-and-partition -freorder-functions -frerun-cse-after-loop -fschedule-insns -fschedule-insns2 -fsched-interblock -fsched-spec -fstore-merging -fstrict-aliasing -fthread-jumps -ftree-builtin-call-dce -ftree-pre -ftree-switch-conversion -ftree-tail-merge -ftree-vrp"
o2flags_list = o2flags.split(" ")

o3flags="-fgcse-after-reload -fipa-cp-clone -floop-interchange -floop-unroll-and-jam -fpeel-loops -fpredictive-commoning -fsplit-loops -fsplit-paths -ftree-loop-distribution -ftree-loop-vectorize -ftree-partial-pre -ftree-slp-vectorize -funswitch-loops -fvect-cost-model -fvect-cost-model=dynamic -fversion-loops-for-strides"
o3flags_list = o3flags.split(" ")


print("\n\nUSING O1 FLAGS\n")
t1=[]
for flag in o1flags_list:
        comp = subprocess.run([compiler, flag, sourcefile], capture_output=True)
        if comp.returncode != 0:
            print('Compilation with this flag failed', flag)
            print('Error message: ', comp.stderr)
        else:
            run = subprocess.run(['./a.out'], capture_output=True)
            print(flag, run.stdout)
            t1.append(retrieve_time(run.stdout))
# now combine all flags
cmd = o1flags_list.copy()
cmd.insert(0, compiler)
cmd.append(sourcefile)
comp = subprocess.run(cmd, capture_output=True)
if comp.returncode != 0:
    print('One of the flags failed')
    print(comp.stderr)
else:
    run = subprocess.run(['./a.out'], capture_output=True)
    print('ALL', run.stdout)
    t1.append(retrieve_time(run.stdout))

x = o1flags_list.copy()
x.append('ALL')
plt.figure(figsize=(15,6))
plt.scatter(x, t1, color='red', marker='o')
plt.xticks(rotation=90);
plt.xlabel('Flags', fontsize=20)
plt.ylabel('Multiplication time (s)', fontsize=16)
plt.yticks(fontsize=14);
plt.title("GCC O1 flags", fontsize=18);
plt.savefig('o1flags.png')




print("\n\nUSING O2 FLAGS\n")
t2=[]
for flag in o2flags_list:
        comp = subprocess.run([compiler, flag, sourcefile], capture_output=True)
        if comp.returncode != 0:
            print('Compilation with this flag failed', flag)
            print('Error message: ', comp.stderr)
        else:
            run = subprocess.run(['./a.out'], capture_output=True)
            print(flag, run.stdout)
            t2.append(retrieve_time(run.stdout))
# now combine all flags
cmd = o2flags_list.copy()
cmd.insert(0, compiler)
cmd.append(sourcefile)
comp = subprocess.run(cmd, capture_output=True)
if comp.returncode != 0:
    print('One of the flags failed')
    print(comp.stderr)
else:
    run = subprocess.run(['./a.out'], capture_output=True)
    print('ALL', run.stdout)
    t2.append(retrieve_time(run.stdout))

x = o2flags_list.copy()
x.append('ALL')
plt.figure(figsize=(15,6))
plt.scatter(x, t2, color='blue', marker='s')
plt.xticks(rotation=90);
plt.xlabel('Flags', fontsize=20)
plt.ylabel('Multiplication time (s)', fontsize=16)
plt.yticks(fontsize=14);
plt.title("GCC O2 flags", fontsize=18);
plt.savefig('o2flags.png')




print("\n\nUSING O3 FLAGS\n")
t3 = []
for flag in o3flags_list:
        comp = subprocess.run([compiler, flag, sourcefile], capture_output=True)
        if comp.returncode != 0:
            print('Compilation with this flag failed', flag)
            print('Error message: ', comp.stderr)
        else:
            run = subprocess.run(['./a.out'], capture_output=True)
            print(flag, run.stdout)
            t3.append(retrieve_time(run.stdout))
# now combine all flags
cmd = o3flags_list.copy()
cmd.insert(0, compiler)
cmd.append(sourcefile)
comp = subprocess.run(cmd, capture_output=True)
if comp.returncode != 0:
    print('One of the flags failed')
    print(comp.stderr)
else:
    run = subprocess.run(['./a.out'], capture_output=True)
    print('ALL', run.stdout)
    t3.append(retrieve_time(run.stdout))

x = o3flags_list.copy()
x.append('ALL')
plt.figure(figsize=(10,6))
plt.scatter(x, t3, color='green', marker='^')
plt.xticks(rotation=90);
plt.xlabel('Flags', fontsize=20)
plt.ylabel('Multiplication time (s)', fontsize=16)
plt.yticks(fontsize=14);
plt.title("GCC O3 flags", fontsize=18);
plt.savefig('o3flags.png')




print("\n\nCOMBINING INDIVIDUAL FLAGS\n")
cmd = o1flags_list.copy()
cmd = cmd + o2flags_list
cmd.insert(0, compiler)
cmd.append(sourcefile)
comp = subprocess.run(cmd, capture_output=True)
if comp.returncode != 0:
    print('One of the flags failed')
    print(comp.stderr)
else:
    run = subprocess.run(['./a.out'], capture_output=True)
    print('O1 + O2', run.stdout)


cmd = o1flags_list.copy()
cmd = cmd + o2flags_list + o3flags_list
cmd.insert(0, compiler)
cmd.append(sourcefile)
comp = subprocess.run(cmd, capture_output=True)
if comp.returncode != 0:
    print('One of the flags failed')
    print(comp.stderr)
else:
    run = subprocess.run(['./a.out'], capture_output=True)
    print('O1 + O2 + 03', run.stdout)




print("\n\n USING O0, O1, O2, O3 DIRECTLY")
cmd = [compiler, '-O0', sourcefile]
comp = subprocess.run(cmd, capture_output=True)
if comp.returncode != 0:
    print('One of the flags failed')
    print(comp.stderr)
else:
    run = subprocess.run(['./a.out'], capture_output=True)
    print('-O0', run.stdout)


cmd = [compiler, '-O1', sourcefile]
comp = subprocess.run(cmd, capture_output=True)
if comp.returncode != 0:
    print('One of the flags failed')
    print(comp.stderr)
else:
    run = subprocess.run(['./a.out'], capture_output=True)
    print('-O1', run.stdout)


cmd = [compiler, '-O2', sourcefile]
comp = subprocess.run(cmd, capture_output=True)
if comp.returncode != 0:
    print('One of the flags failed')
    print(comp.stderr)
else:
    run = subprocess.run(['./a.out'], capture_output=True)
    print('-O2', run.stdout)


cmd = [compiler, '-O3', sourcefile]
comp = subprocess.run(cmd, capture_output=True)
if comp.returncode != 0:
    print('One of the flags failed')
    print(comp.stderr)
else:
    run = subprocess.run(['./a.out'], capture_output=True)
    print('-O3', run.stdout)
