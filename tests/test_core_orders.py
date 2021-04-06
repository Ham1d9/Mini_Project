from unittest.mock import Mock, patch
from src.core_modules.core_orders import (
    fetch_transaction,
    view_orders,
    update_status,
    delete_orders,
)


@patch("src.core_modules.core_db.query")
def test_fetch_transaction(mock_query):

    mock_query.return_value = (
        (
            19,
            "out for delivery",
            "kat",
            "1 manchester road",
            "07345643443",
            "kaily",
            "07453485654",
            4,
        ),
    )
    conn = Mock()
    expected = [
        {
            "status": "out for delivery",
            "customer_name": "kat",
            "customer_address": "1 manchester road",
            "customer_phone": "07345643443",
            "courier_name": "kaily",
            "courier_phone": "07453485654",
            "courier_id": 4,
            "id": 19,
        }
    ]
    actual = fetch_transaction(conn)
    assert expected == actual

@patch("src.core_modules.core_db.add")
@patch("pyinputplus.inputMenu")
@patch("pyinputplus.inputNum")
def test_update_status(mock_num, mock_menu, add):
    state = {
        "orders": [
            {
                "status": "pending",
                "customer_name": "foz",
                "customer_address": "123 lodon",
                "customer_phone": "0756234",
                "courier_name": "ban",
                "courier_phone": "075412",
                "courier_id": "1",
                "id": "1",
            }
        ]
    }

    conn = Mock()

    mock_num.return_value = 0
    mock_menu.return_value = "done"
    expected = {
        "orders": [
            {
                "status": "pending",
                "customer_name": "foz",
                "customer_address": "123 lodon",
                "customer_phone": "0756234",
                "courier_name": "ban",
                "courier_phone": "075412",
                "courier_id": "1",
                "id": "1",
            }
        ]
    }
    actual = update_status(state, conn)
    assert actual == expected


@patch("src.core_modules.core_db.add")
@patch("pyinputplus.inputInt")
def test_delele_order(mock_int,add):

    conn = Mock()
    state = {
        "orders": [
            {
                "id": "1",
                "status": "pending",
                "customer_name": "foz",
                "customer_address": "123 lodon",
                "customer_phone": "0756234",
                "courier_name": "ban",
                "courier_phone": "075412",
                "courier_id": "1",
            }
        ]
    }
    expected = {
        "orders": [
            {
                "id": "1",
                "status": "pending",
                "customer_name": "foz",
                "customer_address": "123 lodon",
                "customer_phone": "0756234",
                "courier_name": "ban",
                "courier_phone": "075412",
                "courier_id": "1",
            }
        ]
    }

    mock_int.return_value = 0

    actuall = delete_orders(state, conn)
