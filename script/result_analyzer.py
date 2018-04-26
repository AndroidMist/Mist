import os
import sys


if __name__ == '__main__' :
    ser_dir = os.path.abspath(sys.argv[1])
    res_dir = os.path.abspath(sys.argv[2])
    sum_dir = os.path.abspath(sys.argv[3])
    misexpose_dir = os.path.abspath(sys.argv[4])
    sers = os.listdir(ser_dir)
    if not os.path.exists(res_dir):
        os.makedirs(res_dir)
    if not os.path.exists(sum_dir):
        os.makedirs(sum_dir)
    if not os.path.exists(misexpose_dir):
        os.makedirs(misexpose_dir)
    command = 'java  -jar lib/MistResultAnalyzer.jar '+ ser_dir +' '+res_dir +' '+sum_dir +' ' +misexpose_dir
    os.system(command)
