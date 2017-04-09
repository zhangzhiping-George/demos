import subprocess

p = subprocess.Popen(['ls -l'], stdin=subprocess.PIPE, stdout=subprcess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'/home/ubunturoot/')
print(output.decode('utf-8'))


