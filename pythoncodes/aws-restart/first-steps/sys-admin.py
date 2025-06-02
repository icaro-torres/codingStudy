import os
import subprocess

# this script is used to test the execution of various shell commands using os.system and subprocess.run

print("--- Executing exercise 1: os.system ---")
os.system("ls") # os.system is used to execute a shell command
print("-" * 40)

print("--- Executing exercise 2: subprocess.run ---")
subprocess.run(["ls"]) # subprocess.run is used to execute a shell command and wait for it to complete
print("-" * 40)

print("--- Executing exercise 3: subprocess.run(['ls', '-l']) ---")
subprocess.run(["ls", "-l"]) # subprocess.run can take a list of arguments
print("-" * 40)

print("--- Executing exercise 4: subprocess.run(['ls', '-l', 'readme.md']) ---")
subprocess.run(["ls", "-l", "readme.md"]) # subprocess.run can also take a list of arguments with a specific file
print("-" * 40)

print("--- Executing exercise 5: uname -a ---")
command_uname = "uname" # i renamed it to avoid confusion with the variable
comandArgument_uname = "-a" # this is the argument for the uname command to get all system information
# uname is a command that prints system information
print(f'Gathering system information with command: {command_uname} {comandArgument_uname}')
subprocess.run([command_uname, comandArgument_uname])
print("-" * 40)

'''
print("--- Executing exercise 6: ps -x ---")
comand_ps = "ps" # i renamed it to avoid confusion with the variable above
comandArgument_ps = "-x" # this is the argument for the ps command to get all processes
print(f'Gathering process information with command: {comand_ps} {comandArgument_ps}')
subprocess.run([comand_ps, comandArgument_ps]) # ps is a command that prints information about running processes
print("-" * 40)
'''

# i had a returning error with the comand above, so i'll try to do it differently

print("--- Executing exercise 7: ps aux ---")
comand_ps_aux = "ps" # i renamed it to avoid confusion with the variable above
comandArgument_ps_aux = "aux" # this is the argument for the ps command to get all processes with detailed information
print(f'Gathering detailed process information with command: {comand_ps_aux} {comandArgument_ps_aux}')
# ps aux is a command that prints information about all running processes
subprocess.run(["ps", "aux"])
print("-" * 40)

print("All the comands executed successfully.")