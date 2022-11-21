import main
from main import Order
import json


def test_bucket():
    assert main.calculateBuckets(19.6) == [1,1,1,3]

def test_write():
    order = Order("Dulux","White","13.00",[1,1,1,3])
    main.saveToJson(order)

