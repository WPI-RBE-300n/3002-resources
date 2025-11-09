# Turtlebot3 Simulation Setup

## Install Turtlebot3

⚠️ **NOTE**: The lab computers already have the (system-wide) Turtlebot3 setup.
So you can skip to [environment configuration](#environment-configuration).

Follow the instructions [here](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup) to set up the Turtlebot3 simulation environment for your user.
(⚠️ **NOTE**: Make sure the `Jazzy` version is selected in the top left corner)

### Environment Configuration

⚠️ **Note**: Make sure ```ROS_DOMAIN_ID``` you set on your host computer is the same as the ```ROS_DOMAIN_ID``` on your turtlebot.

```shell
# To be added to the end of the ~/.bashrc file on your computer and turtlebot3
export ROS_DOMAIN_ID=30
export TURTLEBOT3_MODEL=burger
# or simply run these commands to add them to your ~/.bashrc file
# echo "export ROS_DOMAIN_ID=30" >> ~/.bashrc
# echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
# source ~/.bashrc
```

---
If you have followed the tutorial, you have installed Turtlebot3 under the ```~/turtlebot3_ws``` workspace.
Make sure the ```~/turtlebot3_ws``` workspace is sourced in your terminal.

In this class, you will need to create another workspace for your own code.
This is fine as long as both workspaces are sourced in your terminal.

⚠️ **NOTE**: If you have installed `turtlebot3` packages on your system (i.e., using `apt install`),
you can't build the `turtlebot3_ws` because of name conflicts. So pick one!

## Set Up Simulation

⚠️ **NOTE**: The lab computers already have the (system-wide) Turtlebot3 simulation setup.
So you can skip to [launching the simulation](#launching-the-simulation).

Follow the instructions [here](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/) to set up the Turtlebot3 simulation environment for your user.
(⚠️ **NOTE**: Make sure the `Jazzy` version is selected in the top left corner)

Make sure the ```~/turtlebot3_ws``` workspace is sourced in your terminal after building the `turtlebot3_ws` workspace.

### Launching the Simulation

Empty World:
```shell
ros2 launch turtlebot3_gazebo empty_world.launch.py
```

Turtlebot3 World:
```shell
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Turtlebot3 House:
```shell
ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py
```

