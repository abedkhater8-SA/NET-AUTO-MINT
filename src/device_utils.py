from netmiko import ConnectHandler


def get_interface_status(device, interface_name):
    connection = ConnectHandler(**device)
    connection.enable()

    output = connection.send_command(
        "show ip interface brief",
        use_textfsm=True,
    )

    connection.disconnect()

    for interface in output:
        if interface["interface"] == interface_name:
            return {
                "status": interface["status"],
                "protocol": interface["proto"],
            }

    return None


def interface_is_healthy(interface_data):
    if interface_data is None:
        return False

    return (
        interface_data["status"] == "up"
        and interface_data["protocol"] == "up"
    )