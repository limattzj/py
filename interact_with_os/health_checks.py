import shutil
import psutil


def check_disk_usage(disk: str) -> bool:
    """
    A function checks the percentage of free disk storage.

    Args:
        disk: name of the disk, use '/' for root.

    Returns:
        True if unused disk storage space is more than 20 percent
    """

    # du is a tuple with attributes 'total', 'used', 'free'
    du = shutil.disk_usage(disk)

    # calculate amount of unused disk space as a percentage
    free = du.free / du.total * 100

    return free > 20


def check_cpu_usage():
    """
    A function checks for cpu percent.

    Returns:
        True if cpu usage is less than 75 percent and False otherwise
    """

    usage = psutil.cpu_percent(interval=1)
    return usage < 75


if __name__ == "__main__":
    result = check_disk_usage("/")
    print(result)

