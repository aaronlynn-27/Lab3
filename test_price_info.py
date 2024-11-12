import price_info as price

# Define price_list and quantity_list for testing
price_list = {'apple': 2.5, 'orange': 1.5, 'watermelon': 7.5}
quantity_list = {'apple': 3, 'orange': 2, 'watermelon': 5}

def test_cost_of_fruits():
    test_result = price.cost_of_fruits('apple', 5, price_list)
    expected = 12.5
    assert test_result == expected

def test_total_cost_shopping():
    test_result = price.total_cost_shopping(price_list, quantity_list)
    expected = 48.0
    assert test_result == expected
