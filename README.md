# EVDEMO

With evdemo you can get "raw" access to keyboard and mouse.

it's only for linux. 

## Install

You can you pip to install evdev or one option is take it from apt.

```bash
pip install evdev --user
```

```bash
sudo apt install python3-evdev
```

## Set correct permissions

There is alot bad advice on the internet about how to set permissions for input devices.

The correct way is to add the user to the input group.

```bash
sudo usermod -a -G input the_user
```

To see what groups you are in, run the following command:

```bash
id the_user
```

Then you need to log out and log in again. OR you can run the following command:

```bash
newgrp input
```

This logs you into the input group. You can now run evdev without sudo.

To see that evdev works, run the following command:

```bash
python3 -m evdev.evtest
```
