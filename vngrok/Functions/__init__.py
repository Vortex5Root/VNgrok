import logging
import pexpect
import time


def start_logger(file_name : str):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler(file_name)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    return logger

def run_subprocess(command, stop_event, ssh_password=None):
    run_loggs = start_logger("run_subprocess.log")
    """
    Function to run a subprocess command and terminate it if stop_event is set.
    """
    try:
        # Start the subprocess
        process = pexpect.spawn(command)
        # If the command requires a password, send it
        run_loggs.info(f"Subprocess {command} started.")
        # Loop until the stop_event is set
        while not stop_event.is_set():
            time.sleep(1)
        run_loggs.info(f"Stop event set for subprocess {command}.")
        # Terminate the process
        process.terminate()
        run_loggs.info(f"Subprocess {command} terminated.")
    except pexpect.exceptions.ExceptionPexpect as e:
        run_loggs.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")