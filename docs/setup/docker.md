# RBE3002 Docker Setup

⚠️ NOTE: ROS tools/setups that would require networking and GUI are not supported.
But you can still use it as a development container with all the ros2 tools.
Docker image is adapted from [this](https://github.com/GodOfKebab/ros2-tmotor).

The `ros2-desktop` docker image includes ros2 tools and some other useful tools like `nano` and an ssh server.
The default workspace in the container is `/root/ros2_ws`, which is mapped to `.../3002-resources/docker/ros2_ws` on your host machine.

Download the repo:
```shell
git https://github.com/WPI-RBE-300n/3002-resources.git
cd 3002-resources
```

To build and run the container:
```shell
cd docker
docker compose up ros2-desktop
```

On other terminals, you can ssh into the container by:
```shell
ssh root@localhost -p 2222
# password: goat
```

