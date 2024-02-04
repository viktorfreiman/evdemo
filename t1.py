import evdev
# from pprint import pprint

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

for device in devices:
    # print(device.path, device.name, device.phys)
    # pprint(device.capabilities(verbose=True), indent=4)
    try:
        if device.repeat:
            print(f"Device {device.name} supports repeat events, Keyboard?")
    except SystemError:
        # print(f"Device {device.name} does not support repeat events")
        pass
