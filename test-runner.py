import os
import signal
import subprocess as sp
import sys


def getTestsFromFolder(folderName):
    tests = []
    for file in [file for file in os.listdir(folderName)]:
        if "__init__" not in file and "pyc" not in file:
            tests.append(file.split(".")[0])
    return tests


def runAllTests(folder):
    status = []
    for testFile in getTestsFromFolder(folder):
        child = sp.Popen(["python3", "-m", "unittest", folder + "." + testFile], stdout=sp.PIPE)
        streamdata = child.communicate()[0]
        status.append(child.returncode)
    return 1 if 1 in status else 0


if __name__ == "__main__":
    pid = 0
    lines = open("pid","r").readlines()
    os.remove("pid")
    if len(lines) == 1:
        pid = lines[0].rstrip()
        testsRunnerExitCode = runAllTests("test")
        os.kill(int(pid), signal.SIGKILL)
        sys.exit(testsRunnerExitCode)
    else:
        sys.exit(1)
