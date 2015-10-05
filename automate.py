import os
f_write=open("automate_python.sh",'w')
rootDir = './Lab2'
def fix_escape_char(path):
    correct_path=''
    for char in path:
        if ' ' in char:
            correct_path+='\ '
        elif '(' in char:
            correct_path+='\('
        elif ')' in char:
            correct_path+='\)'
        else:
            correct_path+=char
    return correct_path
            
for dirName, subdirList, fileList in os.walk(rootDir):
        for filename in fileList:
            if ".py" in filename:
                path=dirName+"/"+filename
                correct_path=fix_escape_char(path)
                delimiter_fname="echo '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%';done"
                f_write.write(delimiter_fname+"\n")
                f_write.write("echo "+str(filename)+"\n")
                f_write.write(delimiter_fname+"\n")
                script_run="python3 "+correct_path+"\n"
                cat_command="cat "+correct_path+"\n"
                f_write.write(cat_command)
                delimiter="for i in `seq 1 3`;do echo '*******************************************************************************';done"
                f_write.write(delimiter+"\n")
                f_write.write(script_run)
                empty_space="for i in `seq 1 20`;do echo;done"
                f_write.write(empty_space+"\n")
                
                