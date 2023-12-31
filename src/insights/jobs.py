from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    dictionary_list = []
    with open(path) as file:
        content = csv.DictReader(file)
        for line in content:
            dictionary_list.append(line)
        return dictionary_list


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)

    job_types = set(job["job_type"] for job in jobs if job["job_type"])
    return list(job_types)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    job_list = list(job for job in jobs if job["job_type"] == job_type)
    return job_list
