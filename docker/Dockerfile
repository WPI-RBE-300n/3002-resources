FROM ubuntu:24.04 AS ros2-base

RUN apt update && \
    apt install -y locales && \
    locale-gen en_US en_US.UTF-8 && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
ENV LANG=en_US.UTF-8

RUN apt install -y software-properties-common && \
    add-apt-repository universe

RUN apt install -y curl && \
    export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}') && \
    curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb" && \
    dpkg -i /tmp/ros2-apt-source.deb

RUN apt-get update
RUN apt install -y ros-jazzy-ros-base

WORKDIR /ros2_ws
RUN chsh -s /bin/bash
RUN echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc
RUN echo "[ -f \"/ros2_ws/install/local_setup.bash\" ] && source /ros2_ws/install/local_setup.bash" >> /root/.bashrc
ENV PATH=$PATH:/opt/ros/jazzy/bin/

# Spin forever
CMD tail -f /dev/null

# For desktop, just install additional packages on top of base
FROM ros2-base AS ros2-desktop

RUN apt install -y ros-jazzy-desktop && \
    apt install -y nano openssh-server && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/run/sshd

# Generate SSH host keys
RUN ssh-keygen -A

# Create user
RUN echo 'root:goat' | chpasswd

# SSH configuration
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

CMD ["/usr/sbin/sshd", "-D", "-e"]