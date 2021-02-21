from unittest.mock import Mock, patch
from src.core_modules.core_product import create_products, update_products, delete_products, fetch_products, view_products


# def start_testing(): 

def test_fetch_products():
    expected = []
    actuall = fetch_products()


def test_view_products():
    
    state = {"products":[{"id":1, "product_name":"cat", "quantity":2, "price":2}]}
    
    mockprint=Mock
    
    excepted = {"products":[{"id":1, "product_name":"cat", "quantity":2, "price":2}]}
    actuall = view_products
    



@patch("pyinputplus.inputInt")
@patch("pyinputplus.inputFloat")
@patch("pyinputplus.inputStr")
def test_create_product(mock_str,mock_float,mock_int):
    state=[]
    
    mock_str.side_effect = ["testing"]
    mock_float.side_effect = [1]
    mock_int.side_effect = [1]
    
    mock_add = Mock()
    mock_print = Mock()
    
    expected = []
    actuall = create_products(state)

@patch("pyinputplus.inputInt")
@patch("builtins.input")
@patch("pyinputplus.inputFloat")
@patch("pyinputplus.inputNum") 

def test_update_product(mock_num,mock_float,mock_input,mock_int):
    
    mock_num.side_effect = [0]
    mock_float.side_effect = [1.5]
    mock_int.side_effect = [4]
    mock_input.side_effect = ["kat"]
    state = {"products":[{"id":1, "product_name":"cat", "quantity":2, "price":2}]}
    mock_view_products = Mock()
    mock_add= Mock
    
    expected = {"products":[{"id":1, "product_name":"cat", "quantity":2, "price":2}]}
    actuall = update_products(state)





@patch("pyinputplus.inputNum")
def test_delete_products(fake_input):
    fake_input.side_effect = [0]
    state = {"products":[{"id":1, "product_name":"cat", "quantity":2, "price":2}]}
    expected = {"products":[{"id":1, "product_name":"cat", "quantity":2, "price":2}]}
    
    mock_view_products = Mock()
    mock_add = Mock()
    mock_os_clear = Mock()
    actuall = delete_products(state)

        
# if __name__ == '__main__':
#     start_testing()
