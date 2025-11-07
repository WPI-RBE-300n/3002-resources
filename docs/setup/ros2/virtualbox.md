# 📦 VirtualBox + Ubuntu 24.04 Setup

💻 This is a simple guide to set up Ubuntu 24.04 in VirtualBox for ROS2 development.

## 📥 Downloads

1. Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) for your host OS
2. Download [Ubuntu 24.04 TLS Desktop ISO](https://ubuntu.com/download/desktop) (Noble Numbat)

## 🚀 Setup Steps

### 1. ✨ Create a New Virtual Machine

1. Open VirtualBox and click **New** 🆕
2. Configure the VM:
   - **Virtual machine name and operating system**:
     - **Name**: Ubuntu-ROS2 (or any name you prefer)
     - **ISO Image**: Select the Ubuntu 24.04 ISO you downloaded
     - Keep the rest of the settings as default
   - **Specify virtual hardware**:
     - **Base memory**: Minimum 4GB, Recommended 8GB+ (or half of your host RAM)
     - **Number of CPUs**: Minimum 2, Recommended 4+ (or half of your physical host CPU cores)
   - **Specify virtual hard disk**:
     - **Disk Size**: Minimum 25 GB, Recommended 50 GB+
     - Leave rest as default
   - Then hit **Finish**

### 2. 🐧 Install Ubuntu

1. **Start** the VM ▶️
2. **Follow** the Ubuntu installation wizard:
3. **Wait** for installation to complete ⏳

### 3. 🤖 Install ROS2 Jazzy

📖 See [official docs for installing on Ubuntu](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html).

### 4. ✅ Post-Installation

After installing `ros2`, see:
- 🔧 [Handy commands to run after ROS2 installation](../../post-ros2-install.md)
- 🛠️ [Handy ROS2 commands for debugging](../../handy-ros2-commands.md)
