import sys
from subprocess import Popen

targets = 'listener.py', 'intruder.py'

new_window_command = "cmd.exe /c start".split()

py = [sys.executable]
processes = [Popen(new_window_command + py + [target])  for target in targets]

for proc in processes:
    print(str(proc.pid))
    proc.wait()