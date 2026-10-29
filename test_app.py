from app import calculate_total, apply_discount

def test_calculate_total():
    assert calculate_total(10.0, 5) == 50.0

def test_apply_discount():
    assert apply_discount(100.0, 15) == 85.0
