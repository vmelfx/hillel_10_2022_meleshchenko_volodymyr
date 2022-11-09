# Hillel course (10.2022)

## About
...

## Quick start
 
### Install deps
```bash
# Instal pipenv
pip install pipenv

# Activate virtual env
pipenv shell

# Install deps
pipenv sync
```

#### Additional
```bash
# Regenerate Pipfile.lock
pipenv lock

# Install deps from Pipfile.lock file
pipenv sync

# Pipenv lock & pipenv sync
pipenv update
```
### Rockyou.txt download
You can get this file from git (this is direct download link) :
```
https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
```
Once you download it, you need to put it in your project directory.
For example:
```bash
C:\Users\user\PycharmProjects\your_project\
```