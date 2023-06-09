import subprocess
import os
import sys
def run_scrapper():
   subprocess_files = {'betway.py','misli.py','marathon.py','tuttur.py','unibet.py','10bet.py','888sport.py','nesine.py'}
   for file in subprocess_files:
      print(file)
      subprocess.run(["python", file])
      
run_scrapper()