import platform
import sys

def os_and_sys_version():
    """Returns the current Python version and OS name"""
    python_version = platform.python_version()
    os_name = platform.system()  # This returns 'Windows', 'Linux', etc.
    
    return python_version, os_name

if __name__ == "__main__":
    print(os_and_sys_version())
