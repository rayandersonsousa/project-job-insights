from src.pre_built.counter import count_ocurrences


def test_counter():
    results = count_ocurrences("data/jobs.csv", "FINANCE")
    assert results == 512
