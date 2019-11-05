import os

testfolder = r"\\bvn\idt\idtInstalls\Infrastructure\Ian-Temp\_RevitJournal\20190908_Crash on Remapping P Drive"
#testfolder = r"C:\000"
crashedFiles = []

print(testfolder)

#Change to the test folder
os.chdir(testfolder)

for filename in os.listdir(os.path.join(testfolder)):
    f = open(filename, 'r')
    content = f.read()
    if 'crash' in content:
        crashedFiles.append(filename)

print ('Bad Files as Follows:')
for cf in crashedFiles:
    
    print(cf)

