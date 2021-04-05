from unittest.mock import Mock, patch
from src.core_modules.core_product import (
    create_products,
    update_products,
    delete_products,
    fetch_products,
    view_products,
)


@patch("src.core_modules.core_db.query")
def test_fetch_products(mock_query):
    mock_query.return_value = ((2, "coke cola", 6, 0.8), (26, "water", 8, 1.3))
    mock_conn = Mock()

    expected = [
        {"product_name": "coke cola", "quantity": 6, "price": 0.8, "id": 2},
        {"product_name": "water", "quantity": 8, "price": 1.3, "id": 26},
    ]
    actual = fetch_products(mock_conn)
    assert actual == expected


def test_view_products():

    state = {"products": [{"id": 1, "product_name": "cat", "quantity": 2, "price": 2}]}
    expected = {
        "products": [{"id": 1, "product_name": "cat", "quantity": 2, "price": 2}]
    }
    actual = view_products(state)
    assert actual == expected


@patch("src.core_modules.core_db.add")
@patch("pyinputplus.inputInt")
@patch("pyinputplus.inputFloat")
@patch("pyinputplus.inputStr")
def test_create_product(mock_str, mock_float, mock_int, mock_add):

    conn = Mock()
    state = []
    mock_str.return_value = "green water"
    mock_float.return_value = 2
    mock_int.return_value = 5
    expected = []
    actual = create_products(state, conn)
    assert actual == expected


@patch("src.core_modules.core_db.add")
@patch("pyinputplus.inputInt")
@patch("builtins.input")
@patch("pyinputplus.inputFloat")
@patch("pyinputplus.inputNum")
def test_update_product(mock_num, mock_float, mock_input, mock_int, mock_add):

    conn = Mock()
    mock_num.return_value = 0
    mock_float.return_value = 1.5
    mock_int.return_value = 4
    mock_input.return_value = "kat"
    state = {"products": [{"id": 1, "product_name": "cat", "quantity": 2, "price": 2}]}
    expected = {
        "products": [{"id": 1, "product_name": "kat", "quantity": 4, "price": 1.5}]
    }
    actual = update_products(state, conn)
    assert actual == expected


@patch("src.core_modules.core_db.add")
@patch("pyinputplus.inputNum")
def test_delete_products(fake_input, mock_add):
    fake_input.return_value = 0
    state = {"products": [{"id": 1, "product_name": "cat", "quantity": 2, "price": 2}]}

    conn = Mock()
    expected = {
        "products": [{"id": 1, "product_name": "cat", "quantity": 2, "price": 2}]
    }
    actual = delete_products(state, conn)
    assert actual == expected
