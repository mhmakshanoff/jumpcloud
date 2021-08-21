import subprocess

def pytest_sessionstart(session):
    subprocess.call(['sh', './start-app.sh'])

def pytest_sessionfinish(session, exitstatus):
    subprocess.call(['sh', './stop-app.sh'])
