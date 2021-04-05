# from unittest.mock import Mock, patch
# from src.core_modules.core_orders import fetch_transaction,view_orders,update_status,delete_orders




# def test_fetch_transaction():
    
#     expected = []
#     actuall = fetch_transaction


# def test_view_transaction():
    
#     state = {"orders":[{"status":"pending","customer_name":"foz","customer_address":"123 lodon","customer_phone":"0756234","courier_name":"ban","courier_phone":"075412","courier_id":"1","id":"1"}]}
 
#     mockprint=Mock()
    
#     excepted = {"orders":[{"status":"pending","customer_name":"foz","customer_address":"123 lodon","customer_phone":"0756234","courier_name":"ban","courier_phone":"075412","courier_id":"1","id":"1"}]}
#     actuall = view_orders(state)

# @patch("pyinputplus.inputMenu")
# @patch("pyinputplus.inputNum")
# def test_update_status(mock_num,mock_menu):
#     state = {"orders":[{"status":"pending","customer_name":"foz","customer_address":"123 lodon","customer_phone":"0756234","courier_name":"ban","courier_phone":"075412","courier_id":"1","id":"1"}]}

    
#     mock_num.side_effect = [0]
#     mock_menu.side_effect = ["done"]
    
#     expected = {"orders":[{"status":"pending","customer_name":"foz","customer_address":"123 lodon","customer_phone":"0756234","courier_name":"ban","courier_phone":"075412","courier_id":"1","id":"1"}]}
#     actuall = update_status(state)
    


# @patch("pyinputplus.inputInt")
# def test_delele_order(mock_int):
    
#     state = {"orders":[{"id":"1","status":"pending","customer_name":"foz","customer_address":"123 lodon","customer_phone":"0756234","courier_name":"ban","courier_phone":"075412","courier_id":"1"}]}
#     expected = {"orders":[{"id":"1","status":"pending","customer_name":"foz","customer_address":"123 lodon","customer_phone":"0756234","courier_name":"ban","courier_phone":"075412","courier_id":"1"}]}

#     mock_int.side_effect= [0]
    
#     actuall = delete_orders(state)
    





            
    
    