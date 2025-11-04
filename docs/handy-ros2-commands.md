# ROS2 Commands Cheat Sheet

## Run

```bash
ros2 run <package> <executable>  # Run a node

# Example(s)
ros2 run demo_nodes_cpp talker
ros2 run demo_nodes_cpp add_two_ints_server
```

## Launch

```bash
ros2 launch <package> <launch_file>  # Launch a launch file

# Example(s)
ros2 launch demo_nodes_cpp talker_listener_launch.py
```

## Nodes

```bash
ros2 node list              # List active nodes
ros2 node info <node_name>  # Node details

# Example(s)
ros2 node info /talker
```

## Topics

```bash
ros2 topic list                       # List all topics
ros2 topic list -t                    # List with types
ros2 topic echo <topic>               # Print messages
ros2 topic info <topic>               # Topic details
ros2 topic hz <topic>                 # Message frequency
ros2 topic bw <topic>                 # Bandwidth usage
ros2 topic pub <topic> <type> <data>  # Publish message

# Example(s)
# run on different terminal 'ros2 run demo_nodes_cpp talker'
ros2 topic info /chatter
ros2 topic echo /chatter
# run on different terminal 'ros2 run demo_nodes_cpp listener'
ros2 topic pub /chatter std_msgs/msg/String <tabtab>  # there is a known bug in ros2 that sometimes doesn't automagically complete the tab
```

To get a template message to publish in the terminal, add the following ([what is that bash alias magic?](https://github.com/GodOfKebab/one-liner)) to your `~/.bashrc` and source it:

```bash
# paste this at the end of your ~/.bashrc and source it
alias ros2_msg_template='python3 -c "import base64; import zlib; decoded_string = zlib.decompress(base64.b64decode(b'"'"'eNp1UUtLw0AQvu+vGOuhKUhLewxGKFq9WE96EJWwNpO4sI+wO6kNxf/ubl6mUPcQ2J3vlW+EKo0lcLVjuTUKrHEik6mtNAmFaVnPKxJSkEAHosUWSKlC53iB/3B6ZIdKyaQ1V5IxkYNEHXm3ObfFfgYXCaxiBv6UVmiKJi+BEAfJVapckRKqUnJCuB7E6hJvJrMxaXPgHnWWVqBRSLYOr27hP4vnb+Go44cgeBAULWeMNTwvDgn0Ad+WH4x5dhvxEh6QgL6w/zHYSe4cNCWE54btyIcqGkJQbCHJuLWod2pDdNq3FkNgrkFoR1zvEEw+dhskh3ny5xCdahm9R78AMvC63j560aztqpmHXaRtzCBxuqRo7DBuOZ9M3/VxxP2Zdi0yPOywJIi2JqskPhm6N5XONtYaewVr8ujPirC5z4A7wPhEtxnEPnQlM9CGIBc+b99xU+r02Hc2uPbsOyQupIvhiD9n1voLmGr3ow=='"'"')).decode(); exec(decoded_string)"'

# Example(s)
# run on different terminal 'ros2 run demo_nodes_cpp listener'
ros2_msg_template std_msgs/msg/String
ros2 topic pub /chatter std_msgs/msg/String '
data: 'hello from the terminal'
'
# change the message type to get a template for that type
ros2_msg_template geometry_msgs/msg/TwistStamped
```


## Services

```bash
ros2 service list                          # List services
ros2 service info <service>                # Service info
ros2 service type <service>                # Service type
ros2 service echo <service>                # Print messages
ros2 service call <service> <type> <data>  # Call service

# Example(s)
# run on different terminal 'ros2 run demo_nodes_cpp add_two_ints_server'
ros2 service info /add_two_ints
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 5, b: 3}"
```

## Parameters

```bash
ros2 param list                        # List parameters
ros2 param get <node> <param>          # Get parameter value
ros2 param set <node> <param> <value>  # Set parameter
ros2 param dump <node>                 # Save parameters to file

# Example(s)
# run on different terminal 'ros2 run demo_nodes_cpp add_two_ints_server'
ros2 param dump /add_two_ints_server
```

## Interface (Message Types)

```bash
ros2 interface list         # List all interfaces
ros2 interface show <type>  # Show message structure

# Example(s)
ros2 interface show geometry_msgs/msg/Twist
# run on different terminal 'ros2 run demo_nodes_cpp talker'
ros2 topic list  # use the topic list to get topics
ros2 topic info /chatter  # use the topic info to get the type
ros2 interface show std_msgs/msg/String
# run on different terminal 'ros2 run demo_nodes_cpp add_two_ints_server'
ros2 service list  # use the service list to get services
ros2 service info /add_two_ints  # use the service info to get the type
ros2 interface show example_interfaces/srv/AddTwoInts
```

## Build (Colcon)

```bash
colcon build                          # Build workspace
colcon build --packages-select <pkg>  # Build specific package
source ~/ros2_ws/install/setup.bash   # Source workspace (different from the system-wide setup.bash)
```

## Get Package Prefix Path

For those coming from ROS1, this is not equivalent but can be used to replace `roscd`.

```bash
ros2 pkg prefix demo_nodes_cpp  # Get package prefix path
```

