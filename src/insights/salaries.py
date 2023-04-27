from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    salaries = read(path)

    salary_list = set(
        salary["max_salary"]
        for salary in salaries
        if salary["max_salary"] and salary["max_salary"].isdigit()
    )
    max_salary = max([int(i) for i in salary_list])
    return max_salary


def get_min_salary(path: str) -> int:
    salaries = read(path)

    salary_list = set(
        salary["min_salary"]
        for salary in salaries
        if salary["min_salary"] and salary["min_salary"].isdigit()
    )
    min_salary = min([int(i) for i in salary_list])
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = float(job["min_salary"])
        max_salary = float(job["max_salary"])
        new_value = float(salary)
    except (ValueError, TypeError, KeyError):
        raise ValueError("Invalid values for salaries")

    if min_salary > max_salary:
        raise ValueError("min_salary can't be greater than max_salary")

    return min_salary <= new_value <= max_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    job_list = []
    for job in jobs:
        try:
            if (matches_salary_range(job, salary)):
                job_list.append(job)
        except (ValueError, TypeError, KeyError):
            print("Salary can't be a string")

    return job_list
