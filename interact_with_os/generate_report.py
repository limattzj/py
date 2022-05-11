import csv
from typing import List, Dict


# Read from employees.csv to a list of dictionary that contains each line and
# each key,value pair from each line. Process the list of dictionary to a
# dictionary that count number of employees per department (dict{
# department:number}) and lastly write the processed data to a text file.

def read_employees(csv_file_location: str) -> List[Dict]:
    """A function that parses a csv file and returns a list of dict of data.

    Args:
        csv_file_location: the path to a csv file that contains employee data

    Returns:
        A list of dictionary of employee data.

    """

    # Dialect classes can be registered by name so that callers of the CSV
    # module don't need to know the parameter settings in advance.
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

    # open file
    file_handle = open(csv_file_location)

    employee_file = csv.DictReader(file_handle, dialect='empDialect')

    result = []

    for data in employee_file:
        result.append(data)

    # close file
    file_handle.close()

    return result


def process_data(employee_list: List[Dict]) -> Dict:
    """Count the number of people per department.

    Args:
        employee_list: a list of employee data

    Returns:
        A Dict of department: amount.

    """

    department_list = []
    for data in employee_list:
        department_list.append(data['Department'])

    department_data = {}

    # set() converts duplicates items in dict to distinct items
    # count number of people per department, and store in department_dat as
    # dict with key,value pair {department: number of people}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(
            department_name)

    return department_data


def write_report(department_dict: Dict, report_file: str) -> None:
    """Write processed data to a destination file

    Args:
        department_dict: Dict of processed data that contains number per department.
        report_file: A String of path to a file

    Returns:
    """

    # w+ mode: reading, writing, and overwriting
    with open(report_file, "w+") as f:
        # sort department by alphabetical order and iterate over department_dict
        for k in sorted(department_dict):

            # write key,value pair to file
            f.write(str(k) + ':' + str(department_dict[k]) + '\n')


if __name__ == '__main__':
    employees = read_employees('employees.csv')
    results = process_data(employees)
    write_report(results, 'report.txt')
