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

In `vagrant/` folder, run the following command:
```shell
vagrant up
```

This will install and start the VM (Ubuntu 24.04).

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

Default username is `vagrant` and password is `vagrant`.

Now, follow the [ROS2 installation instructions for Ubuntu 24.04](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html).

Commands that open up windows (like `rqt`) might not work through SSH but will work if you run them from the terminal on the ubuntu desktop on virtualbox.

When you are done, turn off the VM with:
```shell
vagrant halt
```
