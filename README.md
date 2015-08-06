# gelnarBot
A fun bot to spout frivolous insults at people over IRC

Current list of nouns is from Princeton's WordNet version 3.1
http://wordnet.princeton.edu/wordnet/
So if it's full of American things, it's not my fault.




#
# thar be the dragons of how I installed docker and things.
#
echo deb http://get.docker.com/ubuntu docker main | sudo tee /etc/apt/sources.list.d/docker.list

apt-key adv --keyserver pgp.mit.edu --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9

sudo apt-get update
sudo apt-get install -y lxc-docker-1.6.2


sudo easy_install docker-compose
