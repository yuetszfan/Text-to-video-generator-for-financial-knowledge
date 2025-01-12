# setup.py
import os

def install_python():
    os.system("sudo apt-get update -y")
    os.system("sudo apt-get install -y python3.11")
    os.system("sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1")
    os.system("sudo update-alternatives --config python3")
    os.system("sudo apt-get install -y python3.11-distutils")
    os.system("wget https://bootstrap.pypa.io/get-pip.py")
    os.system("python3.11 get-pip.py")
    os.system("pip install moviepy requests")

if __name__ == "__main__":
    install_python()
