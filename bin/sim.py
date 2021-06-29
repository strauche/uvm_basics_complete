#! /usr/bin/env python3

import sys
import os
import subprocess

################################################################################
# functions
################################################################################
def set_path (dirpath, basename):
  path = os.path.join (dirpath, basename)
  if not os.access (path, os.F_OK):
    print ('INFO: creating path:', path)
    # make the directory
    command = ['mkdir','-p',path]
    run_cmd (command)
  else:
    print ('INFO:found path:', path)
  return path


##################################################
# run system command, returns results in List
##################################################
def run_cmd(cmd, echo=False, logfile=None):
  #sys.stdout.write('Running command \"%s\"\n' % cmd)
  # capture_output not in python 3.6
  #result = subprocess.run (cmd, capture_output=True, text=True, shell=False)

  print ('Running', ' '.join(cmd))
  result = subprocess.run (cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8', shell=False)

  if logfile:
    fhw = open(logfile,"w")
    fhw.write (result.stdout)

  # echo cmd stdout to screen 
  if echo:
    print (result.stdout)

  # exit if return status is non-zero
  if result.returncode:
    print ('ERROR: running ', cmd, '\n')
    fhw = open('run.stderr',"w")
    fhw.write (result.stderr)
    print (result.stdout)
    print (ThisFile, "ERROR: exiting program")
    sys.exit (result.returncode)

  lines = []
  if result.stdout:
    lines = result.stdout.split('\n')
    lines.remove('')
  return lines


################################################################################
# run main program
################################################################################
# global program identifier (sim.py)
ThisFile = os.path.basename (__file__)

# command line args
if len(sys.argv) != 2:
  print ('Error: sim.py <testname>')
  sys.exit()
else:
  testname = sys.argv[1]

# set environment
HOME = os.environ['HOME']
QUESTA_UVM_HOME = os.environ['QUESTA_UVM_HOME']
QUESTA_UVM_PKG  = os.environ['QUESTA_UVM_PKG']

# set project directory
#PROJ_HOME = HOME + '/verif_academy/uvm_basics/hello_world'
PROJ_HOME = HOME + '/verif_academy/uvm_basics/complete'
# set env var PROJ_HOME
os.environ['PROJ_HOME'] = PROJ_HOME

# traverse directories from cwd, upwards until PROJ_HOME is found
# note that commands are run from PROJ_HOME
CWD = os.getcwd()
while CWD != PROJ_HOME:
  CWD = os.path.dirname(CWD)
  if (CWD == HOME) or (CWD == '/'):
    print ('ERROR: PROJ_HOME', PROJ_HOME, 'not found')
    sys.exit()
  os.chdir (CWD)

if CWD != PROJ_HOME:
  print ('ERROR: PROJECT_HOME not found', PROJ_HOME)
  sys.exit()
else:
  print ('PROJ_HOME found at', CWD)

# define PROJ local vars and env vars for directory structure
PROJ_BIN = set_path (PROJ_HOME, 'bin')
os.environ ['PROJ_BIN'] = PROJ_BIN
PROJ_DUT = set_path (PROJ_HOME, 'dut')
os.environ ['PROJ_DUT'] = PROJ_DUT

PROJ_SIM = set_path (PROJ_HOME, 'sim')
set_path (PROJ_SIM, testname)
#os.environ ['PROJ_SIM'] = PROJ_SIM

PROJ_TB  = set_path (PROJ_HOME, 'tb')
#os.environ ['PROJ_TB'] = PROJ_TB

# are these needed?
# define TB local vars and env vars for directory structure
TB_ENV   = set_path (PROJ_TB, 'env')
TB_TOP   = set_path (PROJ_TB, 'top')
TB_MY    = set_path (PROJ_TB, 'my')
TB_TESTS = set_path (PROJ_TB, 'tests')


##filelist 
Filelist  = [os.path.join(PROJ_DUT,'dut.sv')]
Filelist += [os.path.join(TB_TOP,'dut_if.sv')]
Filelist += [os.path.join(TB_MY ,'my_pkg.sv')]
Filelist += [os.path.join(TB_ENV,'env_pkg.sv')]
Filelist += [os.path.join(TB_TESTS,'tests_pkg.sv')]
Filelist += [os.path.join(TB_TOP,'top.sv')]

# build the qrun command
command = ['qrun']
command += Filelist

# vlog,vsim, qrun log files
command += ['-vlog.log', '%s/%s/vlog.log' % (PROJ_SIM, testname)]
command += ['-vsim.log', '%s/%s/vsim.log' % (PROJ_SIM, testname)]
command += ['-logfile',  '%s/%s/qrun.log' % (PROJ_SIM, testname)]

command += ['-timeout', '2m']
command += ['-uvm', '-uvmhome', QUESTA_UVM_HOME, '-uvmexthome', QUESTA_UVM_PKG]
command += ['-top','top']
command += ['-verbose']
#command += ['-script', 'script.sim.py']
command += ['+UVM_TESTNAME=' + testname]
command += ['-outdir', os.path.join(PROJ_SIM,testname)]

lines = run_cmd (command)
for line in lines:
  print (line)

#qrun \
#  [filelist] \
#  -uvm -uvmhome $QUESTA_UVM_HOME \
#  -uvmexthome $QUESTA_UVM_PKG \
#  -top top \
#  -verbose \
#  +UVM_TESTNAME=test3 \
#  -outdir os.path.join (PROJ_SIM, test3)
