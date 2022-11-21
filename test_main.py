import main


def test_bucket():
    assert main.calculateBuckets(19.6) == [1,1,1,2]
