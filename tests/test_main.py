from main import os_and_sys_version

def test_os_and_sys_version():
    """Function calling os_and_sys_version"""
    python_version, os_name = os_and_sys_version()
    python_version_check = ["3.7", "3.8", "3.9", "3.10", "3.11"]
    os_name_check = ["Windows", "Linux"]

    # Allowing any version starting with 3.7, 3.8, 3.9, 3.10, or 3.11
    major_version = ".".join(python_version.split(".")[:2])  # Only keep major and minor version
    assert major_version in python_version_check
    
    # if environment has an OS installed
    if os_name is not None:
        assert os_name in os_name_check

if __name__ == "__main__":
    test_os_and_sys_version()
