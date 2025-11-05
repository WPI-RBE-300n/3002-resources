# Remote Setup


You can set up your laptop to use the lab computer as a server/bridge between your laptop and the turtlebot.

## Network Diagram:

<p align="center">
<img src="https://raw.githubusercontent.com/WPI-RBE-300n/3002-resources/refs/heads/main/docs/figures/remote-lab-computer.drawio.png" height="700" alt="demo">
</p>

## How?

1. You can set up your IDE on your laptop to automatically upload files to the lab computer using `scp` or `rsync`.
To `ssh` into the lab computers, the username is your wpi username, and address is known (in the format `ak120d-xx.wpi.edu`).
2. You can also use `ssh` to connect to the lab computer from your laptop and run commands on it.
3. If you set up your `~/.bashrc`, you can even run the GUI applications.
In this case, you would run the tool/application on the lab computer over ssh, and the window would appear on the lab computer.
If you want the GUI applications to display on your laptop, you would need to set up X forwarding.

In the `~/.bashrc` of the lab computer, you can add the following:
```shell
export DISPLAY=:0
```

After installing `ros2`, see:
- [Handy commands to run after ROS2 installation](../../post-ros2-install.md)
- [Handy ROS2 commands for debugging](../../handy-ros2-commands.md)
