import subprocess

subprocess.call(["virtualenv --python=python3 ../env"], shell=True)
subprocess.call(["source ../env/bin/activate"], shell=True)
subprocess.call(["pip install --upgrade pip"], shell=True)
subprocess.call(["pip install flask"], shell=True)
subprocess.call(["pip install Flask-Pymongo"], shell=True)
subprocess.call(["pip install semantria_sdk"], shell=True)




