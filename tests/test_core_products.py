from unittest.mock import Mock, patch
from src.core_modules.core_product import create_products, update_products, delete_products

# unit testing with patch without injections 

@patch("builtins.input")
def test_create_product(mock_input):
    product_list=[]
    
    mock_input.side_effect = ["cat", 2]
    mock_save_products = Mock()
    
    expected = [{"name":"cat", "price":2 }]
    actuall = create_products(product_list)
    
    
@patch("builtins.input")    
def test_update_product(fake_input):
    product_list = [{"name" : "cat", "Price":2}]
    
    mock_save_products = Mock()
    mock_view_products = Mock()
    
    fake_input.side_effect = [0,"Ulia", 1.2]
    
    expected = [{"name":"Ulia", "price":1.2 }]
    actuall = update_products(product_list)


@patch("builtins.input")
def test_delete_products(fake_input):
    
    product_list = [{"name" : "cat", "Price":2}, {"name" : "cat", "Price":2}]
    expected = [{"name" : "cat", "Price":2}]
    mock_save_products = Mock()
    mock_view_products = Mock()
    
    fake_input.side_effect = [1]
    actuall = delete_products(product_list)
    
    
    
    