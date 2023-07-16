import subprocess

commands = [
    'cd probable-chainsaw',
    'pip install git+https://github.com/deathlyface/python-tradingview-ta.git',
    'pip install tradingview_ta --upgrade',
    'pip install requests websocket-client',
    'pip install -r requirements.txt',
    'python setup.py install',
    'pip install iqoptionapi --upgrade',
    'pip install pandas',
    'pip install numpy',
    'pip install python-math'
]

for command in commands:
    subprocess.call(command, shell=True, stderr=subprocess.DEVNULL)
