# 🌀 Cyclone DDS Setup

In this class, we use Cyclone DDS for communication between our robots and our host PC.

## 🤖 Talking to TurtleBot

All our TurtleBots are named after Smash Brothers characters and registered with the domain name following the pattern:

```
mario.dyn.wpi.edu
```

## 🔐 SSH into TurtleBot

🔑 **Login Credentials**: See [TurtleBot login information](https://canvas.wpi.edu/courses/78300/pages/talking-to-turtlebot) for usernames and passwords.

To log into a TurtleBot from your computer over the WPI network:

```bash
# To be executed on your computer
ssh ubuntu@mario.dyn.wpi.edu
# After entering password, you should see a prompt like:
# ubuntu@turtlebot:~$ # any command you type here will be executed on the robot
```

⚠️ **Note**: Usually the robot boots and gets connected to the WPI network and assigned its domain name within 5 minutes of being turned on.
If the name still doesn't resolve after 10 minutes, it can be helpful to connect with the robot using its IP address instead.
To find the robot's IP address, plug it into a monitor and keyboard and run:
```bash
# To be executed on your turtlebot
hostname -I
```

## ⚙️ Configuring Host PC to Find TurtleBot on WPI Network

### 1. Install Cyclone on the host computer

```bash
# To be executed on your computer (turtlebot is already set up with Cyclone DDS)
sudo apt install ros-jazzy-rmw-cyclonedds-cpp
```

### 2. Download and Edit the Cyclone Config File

Download the Cyclone config file template from [here](../../../misc/config.xml).

Place the cyclone config in your home directory (`~/config.xml`) and configure it for your robot's domain/IP address.
This tells Cyclone to turn off multicast and instead only reach out to computers listed in the peers list (i.e., your robot and your own laptop).

Then, edit the `config.xml` file to include your robot's domain address (replace `SMASH_CHARACTER` with your robot's name).

### 3. Configure ROS2 to use Cyclone DDS

⚠️ **Note**: Make sure ```ROS_DOMAIN_ID``` you set on your host computer is the same as the ```ROS_DOMAIN_ID``` on your turtlebot.

```bash
# To be added to the end of the ~/.bashrc file on your computer (turtlebot is already set up with Cyclone DDS)
export ROS_DOMAIN_ID=30  
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export CYCLONEDDS_URI=~/config.xml
# or simply run these commands to add them to your ~/.bashrc file
# echo "export ROS_DOMAIN_ID=30" >> ~/.bashrc
# echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc
# echo "export CYCLONEDDS_URI=~/config.xml" >> ~/.bashrc
# source ~/.bashrc
```
