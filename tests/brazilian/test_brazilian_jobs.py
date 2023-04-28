from src.pre_built.brazilian_jobs import read_brazilian_file

expectedResult = {"title": "Maquinista", "salary": "2000", "type": "trainee"}


def test_brazilian_jobs():
    results = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    assert results[0] == expectedResult
