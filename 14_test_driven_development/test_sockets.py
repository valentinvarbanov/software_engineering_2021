import sockets

def test_create_IP():
    address = sockets.IPAdress('0.0.0.0')
    assert isinstance(address, sockets.IPAdress)

def test_valid_ip():
    address = sockets.IPAdress('0.0.0.0')
    assert address.is_valid()
    address = sockets.IPAdress('127.0.0.1')
    assert address.is_valid()
    
def test_invalid_IP():
    address = sockets.IPAdress('----')
    assert not address.is_valid()
    address = sockets.IPAdress('256.0.0.0')
    assert not address.is_valid()

def test_private_IP():
    address = sockets.IPAdress('10.10.10.10')
    assert address.is_private()
    address = sockets.IPAdress('192.168.10.10')
    assert address.is_private()

def test_public_IP():
    address = sockets.IPAdress('0.0.0.0')
    assert address.is_public()



