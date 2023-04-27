from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    industries = read(path)

    indutry_list = set(
        industry["industry"]
        for industry in industries
        if industry["industry"]
    )
    return list(indutry_list)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industry_list = list(job for job in jobs if job["industry"] == industry)
    return industry_list
