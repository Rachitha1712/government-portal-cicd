from app import service_available

def test_aadhaar():
    assert service_available("Aadhaar") == True

def test_passport():
    assert service_available("Passport") == True

def test_invalid_service():
    assert service_available("DrivingLicense") == False