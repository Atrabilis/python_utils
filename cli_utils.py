import subprocess
import platform

def clear_shell():
    """
    Clear the console screen depending on the operating system.

    This function detects the operating system and clears the console screen accordingly.
    For Windows (NT-based systems), it uses the 'cls' command. For POSIX-based systems
    (e.g., Linux or macOS), it uses the 'clear' command. If the operating system is not
    recognized, it prints a message indicating that.

    :return: None
    """
    operative_system = platform.system()

    if operative_system == "Windows":
        subprocess.run("cls", shell=True)
    elif operative_system == "Linux" or operative_system == "Darwin":
        subprocess.run("clear", shell=True)
    else:
        print("Unrecognized operating system")