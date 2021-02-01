from src.core_modules.core_orders import create_orders,delete_orders


def test_create_orders():
    
    mock_order = [
        {
        "customer_name": 'Jon',
        "customer_address": "123, london address, england",
        "customer_phone": 734234432,
        "courier": 2,
        "status": 'done'
    }
    ]
    
    
    
    def mock_input(ainput):
        if ainput == "Name: ":
            return 'Kat'
        elif ainput == "Address: ":
            return '123, manchester road, manchester'
        elif ainput == "phone: ":
            return 76543217
        elif ainput == "courier: ":
            return 3
        else:
            return 'done'
            
    def mock_save_orders(anything):
        pass
        
    expected = [
        {
        "customer_name": 'Jon',
        "customer_address": "123, london address, england",
        "customer_phone": 734234432,
        "courier": 2,
        "status": 'done'
    }, 
     {
        "customer_name": 'Kat',
        "customer_address": '123, manchester road, manchester',
        "customer_phone": 76543217,
        "courier": 3,
        "status": 'done'
    }
     ]
    
    
    actual = create_orders(mock_order,mock_input,mock_save_orders)
    assert expected == actual
    print('create order testing = passed')

test_create_orders()

def test_delele_order():
    
    mock_order = [
        {
        "customer_name": 'Jon',
        "customer_address": "123, london address, england",
        "customer_phone": 734234432,
        "courier": 2,
        "status": 'done'
    }, 
     {
        "customer_name": 'Kat',
        "customer_address": '123, manchester road, manchester',
        "customer_phone": 76543217,
        "courier": 3,
        "status": 'done'
    }
     ]
    
    expected = [
        {
        "customer_name": 'Jon',
        "customer_address": "123, london address, england",
        "customer_phone": 734234432,
        "courier": 2,
        "status": 'done'
    } 
    ]
    
    def mock_save_orders(anything):
        pass
        
    def mock_view_orders(anything):
        pass
    def mock_input(anything):
        return 1
    
    
    actuall = delete_orders(mock_order,mock_view_orders,mock_input,mock_save_orders)
    assert actuall == expected
    print ('delete order test: passed')
    
test_delele_order()

def test_update_order():
    
    mock_order = [
        {
        "customer_name": 'Jon',
        "customer_address": "123, london address, england",
        "customer_phone": 734234432,
        "courier": 2,
        "status": 'done'
    }, 
     {
        "customer_name": 'Kat',
        "customer_address": '123, manchester road, manchester',
        "customer_phone": 76543217,
        "courier": 3,
        "status": 'done'
    }
     ]
    
    