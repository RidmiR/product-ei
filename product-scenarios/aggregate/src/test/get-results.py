import shutil
import os

cwd = os.getcwd()

dest=cwd+'/aggregate/test-result'
os.mkdir(dest)

# read all the TEST-TestSuite.xml and write the file paths to the new text file
#  to get the count of the testsuit.xml files
filepath = open(cwd+'/aggregate/path.txt', 'w')
for dirpath, dirnames, filenames in os.walk(cwd):
    for filename in filenames:
        if filename == "TEST-TestSuite.xml":
            filename = os.path.join(dirpath, filename)
            print(filename)
            filepath.write('\n' + filename)
filepath.close()

# get the TEST-TestSuite.xml file count
count = len(open(cwd+'/aggregate/path.txt').readlines(  ))

# rename the TEST-TestSuite.xml files by adding a index as a suffix and
# copying TEST-TestSuite.xml file to test-result folder inside aggregate
ii = 1
while ii < count :
    for dirpath, dirnames, filenames in os.walk(start):
        for filename in filenames:
            if filename == "TEST-TestSuite.xml":
                old_name = os.path.join(dirpath, filename )
                dir_path = os.path.join(dirpath)
                base, extension = os.path.splitext(filename)
                newname = os.path.join(dirpath, base + "_" + str(ii) + extension)
                os.chdir(dir_path)
                os.rename(old_name,newname)
                shutil.copy(newname, dest)
                ii = ii + 1
                break
quit()


