
import sys,os

reason_map=dict()
result_map = dict()
fn_map=set()

fn = "result/mist_result"
fw = open(fn+".txt", "w")
mis_file_dir = os.path.abspath(sys.argv[1]).strip()
mis_files= os.listdir(mis_file_dir)

for mis_file in mis_files:
	command = "swipl -f eaclassifier.pl -s " + mis_file_dir +os.path.sep+mis_file+" -g solve -t halt"
	string = "filename: "+mis_file +"\n"
	lines = os.popen(command).readlines()
	for line in lines:
		string+=line
	fw.write(string+"\n")
fw.close()

f = open(fn+".txt", "r")
lines = f.readlines()
f.close()

sum=0
i=0
filename=""
while(i<len(lines)):
	line=lines[i].strip()
	if "0 mainAct" in line:
		i=i+3
		continue
	if "filename: " in line :
		filename = line.split("filename: ")[1].split("_")[0]
		
	if "reason: " in line :
		reason = line.split("reason: ")[1]
		if reason in reason_map:
			reason_map[reason] +=1
		else:
			reason_map[reason] =1
			
	if "result:" in line :
		sum+=1
		result = line.split("result: ")[1]		
		if result in result_map:
			result_map[result] +=1
		else:
			result_map[result] =1
		if"IA" in result:
			fn_map.add(filename)
	i+=1
	
print "number of app contains IA",len(fn_map)
fw= open(fn+"_sum.txt","w")
print "sum", sum

print "reason_map:"
for key in reason_map.keys():
	print key, reason_map[key]
	fw.write(key+"\t\t")
	fw.write(str(reason_map[key]) +"\t\t")
	fw.write(str(1.0*reason_map[key]/sum )+"\n")
	
fw.write("\n")
print ""

print "result_map:"
for key in result_map.keys():
	print key, result_map[key]
	
	fw.write(key+"\t\t")
	fw.write(str(result_map[key]) +"\t\t")
	fw.write(str(1.0*result_map[key]/sum )+"\n")
	

fw.close()
