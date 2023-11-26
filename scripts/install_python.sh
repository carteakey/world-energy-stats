echo "deb http://archive.debian.org/debian stretch main" > /etc/apt/sources.list
apt update
apt-get install -y software-properties-common
add-apt-repository universe
apt update
apt install -y python3
apt install -y python3-pip
python3 -m pip install pandas