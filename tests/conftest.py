import subprocess

def pytest_sessionstart(session):
    subprocess.call(['sh', 'bin/start-app.sh'])

def pytest_sessionfinish(session, exitstatus):
    subprocess.call(['sh', 'bin/stop-app.sh'])
