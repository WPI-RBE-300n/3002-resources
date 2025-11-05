# Vagrant Setup

See [vagrant](https://developer.hashicorp.com/vagrant/intro).
You can use this to set up a VM for development/testing.
If you set up your networking properly (in `vagrant/Vagrantfile`), you can use this to connect to the robot.

Install [Vagrant](https://developer.hashicorp.com/vagrant/install) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads).

Download the repo:
```shell
git clone https://github.com/WPI-RBE-300n/3002-resources.git
cd 3002-resources
```

Edit the `vagrant/Vagrantfile` to customize the VM (# of CPUs, RAM, disk space, etc.).

For disk size setting to work, install the plugin:
```shell
vagrant plugin install vagrant-disksize
```

⚠️ NOTE: For all the respective `vagrant` commands to work, you need to be in the `vagrant/` folder.

Run the following command to pull and spin up the VM ([bento/ubuntu-24.04](https://portal.cloud.hashicorp.com/vagrant/discover/bento/ubuntu-24.04)):
```shell
vagrant up
```

You can ssh into the VM with:
```shell
vagrant ssh
```

Then run these commands and reboot to enable the desktop:
```shell
sudo apt update
sudo apt install -y ubuntu-desktop
sudo reboot
```

It might take some time for the vm to boot up after `ubuntu-desktop` is installed.
Default username is `vagrant` and password is `vagrant`.

Now, follow the [ROS2 installation instructions for Ubuntu 24.04](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html).

Commands that open up windows (like `rqt`) might not work through SSH but will work if you run them from the terminal on the ubuntu desktop on virtualbox.

After installing `ros2`, see:
- [Handy commands to run after ROS2 installation](../../post-ros2-install.md)
- [Handy ROS2 commands for debugging](../../handy-ros2-commands.md)

When you are done, turn off the VM with:
```shell
vagrant halt
```

To spin it back up:
```shell
vagrant up
```

⚠️ If you want to destroy everything and start from scratch:
```shell
vagrant destroy  # or remove the vm from virtualbox
```
