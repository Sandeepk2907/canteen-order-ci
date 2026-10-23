import pytest

from order import calculate_total


def test_zero_subtotal():
    assert calculate_total(0) == 0


def test_small_order_gst_only():
    # 100 + 5% GST = 105
    assert calculate_total(100) == 105.00


def test_exactly_300_gets_no_discount():
    # boundary: 300 is NOT above 300 -> 300 * 1.05
    assert calculate_total(300) == 315.00


def test_just_above_300_gets_discount():
    # 301 * 0.9 * 1.05 = 284.445 -> 284.45 (rounded)
    assert calculate_total(301) == pytest.approx(284.45, abs=0.01)


def test_large_order_discount_and_gst():
    # 500 * 0.9 = 450 ; 450 * 1.05 = 472.5
    assert calculate_total(500) == 472.50


def test_negative_subtotal_raises():
    with pytest.raises(ValueError):
        calculate_total(-1)
