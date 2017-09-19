sudo apt-add-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -yqq ansible
sudo apt-get install -yqq python-pip
sudo -H pip install boto
git clone https://github.com/hd150795/ansible-playbook.git
cp encrypts/python_script.py ansible-playbook
cp encrypts/key.pem ansible-playbook
cd ansible-playbook
python python_script.py
ansible-playbook -i inventory gangliabook.yml
