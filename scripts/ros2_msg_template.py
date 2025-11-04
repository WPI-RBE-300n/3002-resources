import sys
from rosidl_runtime_py.utilities import get_message
from rosidl_runtime_py import message_to_yaml

if len(sys.argv) != 2:
    print("Usage: ros2_msg_template <message_type>")
    print("Example: ros2_msg_template geometry_msgs/msg/Twist")
    sys.exit(1)

msg_type = sys.argv[1]

try:
    # Get the message class from the type string
    msg_class = get_message(msg_type)

    # Create an instance of the message
    msg_instance = msg_class()

    # Convert to YAML and print
    yaml_string = message_to_yaml(msg_instance)
    print(f"'\n{yaml_string}'")

except (ModuleNotFoundError, AttributeError) as e:
    print(f"Error: Could not find message type '{msg_type}'")
    print(f"Details: {e}")
    sys.exit(1)