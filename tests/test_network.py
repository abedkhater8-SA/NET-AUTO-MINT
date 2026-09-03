from src.device_utils import get_interface_status, interface_is_healthy


router1 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.96",
    "username": "admin",
    "password": "Admin@123",
    "secret": "Admin@123",
}


def test_router_interface_is_healthy():
    interface_data = get_interface_status(
        router1,
        "Ethernet0/0",
    )

    assert interface_data is not None
    assert interface_is_healthy(interface_data) is True