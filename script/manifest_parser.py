#/usr/bin/python
#coding=utf-8

import os
import sys
import time
import platform
import shutil

def get_apk_name(s) :
    ss = s.split(os.path.sep)[-1]
    index = ss.rfind('.')
    return ss[0:index]

if __name__ == '__main__' :
    apks_dir = os.path.abspath(sys.argv[1]).strip()
    manifest_dir = os.path.abspath(sys.argv[2]).strip()
    res_dir = os.path.abspath(sys.argv[3]).strip()
    
    if not os.path.exists(manifest_dir):
        os.makedirs(manifest_dir)
    if not os.path.exists(res_dir):
        os.makedirs(res_dir)
        
    decompile_log = "result/decompile_log.txt"
    if not os.path.exists(decompile_log):
        os.mknod(decompile_log) 
    log_file = open(decompile_log, 'a')

    suc_parse_count = 0
    dec_time = 0
    parse_time = 0

    # traverse apks 
    files = os.listdir(apks_dir)
    for f in files :
        mpFileName = f
        f = f.replace(' ', '\ ').replace('[', '\[').replace(']', '\]').replace('(', '\(').replace(')', '\)')
        apk_path = apks_dir + os.path.sep + f
        apk_name = get_apk_name(apk_path)
        
        # decompile
        command = 'java -jar lib/apktool_2.3.1.jar d -o tmp/ -p tmp2/ -f ' + apk_path
        print command
        t1 = time.time()
        os.system(command)
        t2 = time.time()
        dec_time += t2 - t1

        if not os.path.exists('tmp/AndroidManifest.xml') :
            log_file.write('[No manifest] ' + apk_path + os.linesep)
            continue
        else:
            if not os.path.exists(manifest_dir+os.path.sep+apk_name+"_manifest.xml") :
                shutil.copy('tmp/AndroidManifest.xml',manifest_dir+os.path.sep+apk_name+"_manifest.xml") 
            if not os.path.exists(res_dir+os.path.sep+apk_name+"_res") :
                shutil.copytree('tmp/res',res_dir+os.path.sep+apk_name+"_res") 
            
        if not os.path.exists('tmp/AndroidManifest.xml') :
            log_file.write('[No manifest] ' + apk_path + os.linesep)
            continue

        suc_parse_count += 1


        # rm tmp tmp2
        sysstr = platform.system()
        if(sysstr =="Windows"):
            shutil.rmtree("tmp")
            shutil.rmtree("tmp2")
        elif(sysstr == "Linux"):
            command = 'rm -r tmp tmp2'
            print command
            os.system(command)
            
    log_file.write('[Parse] Parse ' + str(suc_parse_count) + ' app(s) successfully' + os.linesep)
    log_file.write('[Time] dec_time: ' + str(dec_time) + 's parse_time: ' + str(parse_time) + 's')
    log_file.close()
