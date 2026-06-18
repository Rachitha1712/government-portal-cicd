def service_available(service):

    services = [
        "Aadhaar",
        "Passport",
        "Tax",
        "Certificate"
    ]

    return False


if __name__ == "__main__":

    service = input("Enter Service Name: ")

    if service_available(service):
        print("Service Available")
    else:
        print("Service Not Available")