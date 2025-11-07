# 🐳 Docker Setup

⚠️ **NOTE**: This setup should work fine for individual labs and signoffs. However, ROS tools that require networking (communicating with physical TurtleBots) and GUI need additional setup.

You can use this as a development container with all the ros2 tools. If you need to communicate with real robots or use GUI tools, you'll need to configure X forwarding and docker networking.

Dockerfile is adapted from [this](https://github.com/GodOfKebab/ros2-tmotor).

📖 See [docker](https://docs.docker.com/get-started/docker-overview/).
The `ros2-desktop` docker image includes ros2 tools and some other useful tools like `nano` and an ssh server.
The default workspace in the container is `/root/ros2_ws`, which is mapped to `.../3002-resources/docker/ros2_ws` on your host machine.

📥 Download the repo:
```shell
git clone https://github.com/WPI-RBE-300n/3002-resources.git
cd 3002-resources
```

🚀 To build and run the container:
```shell
cd docker
docker compose up ros2-desktop
```

🔌 On other terminals, you can ssh into the container by:
```shell
ssh root@localhost -p 2222
# password: goat
```

✅ After logging in, see:
- 🔧 [Handy commands to run after ROS2 installation](../../post-ros2-install.md)
- 🛠️ [Handy ROS2 commands for debugging](../../handy-ros2-commands.md)

