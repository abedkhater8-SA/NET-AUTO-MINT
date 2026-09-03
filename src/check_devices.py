from device_utils import get_device_status


routers = [
    {
        "device_type": "cisco_ios",
        "host": "10.1.1.96",
        "username": "admin",
        "password": "Admin@123",
        "secret": "Admin@123",
    },
    {
        "device_type": "cisco_ios",
        "host": "10.1.1.98",
        "username": "admin",
        "password": "Admin@123",
        "secret": "Admin@123",
    },
    {
        "device_type": "cisco_ios",
        "host": "10.1.1.99",
        "username": "admin",
        "password": "Admin@123",
        "secret": "Admin@123",
    },
]


for router in routers:
    status = get_device_status(router)
    print(status)