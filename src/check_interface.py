from device_utils import get_interface_status, interface_is_healthy

router1 = {
    "device_type": "cisco_ios",
    "host": "10.100.100.33",
    "username": "admin",
    "password": "Admin@123",
    "secret": "Admin@123",
}


interface_name = "Ethernet0/0"

interface_data = get_interface_status(
    router1,
    interface_name,
)

print(f"Interface data: {interface_data}")

if interface_is_healthy(interface_data):
    print(f"{interface_name} is healthy")
else:
    print(f"{interface_name} is NOT healthy")