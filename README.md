<<<<<<< HEAD
<<<<<<< HEAD
BattleSnake 2017
================
=======
# BattleSnake 2018
>>>>>>> 814cb88d2d5f74b169c93678edd562fd6996f207

## Presented by [Sendwithus](https://www.sendwithus.com), in partnership with [GitHub](https://github.com/).

_March 3th, 2018 at the Victoria Conference Centre._

BattleSnake is a programming competition held in Victoria, BC.

Teams program web-based AIs for the classic arcade game "Snake". Multiple teams compete on the same board at the same time, and the winner is the last team slithering!

__Looking for event info? Want to register?__ Visit [www.battlesnake.io](http://www.battlesnake.io).

__Need help? Have questions?__ Email [battlesnake@sendwithus.com](mailto:battlesnake@sendwithus.com).

## Documentation

### [API Reference](https://github.com/sendwithus/battlesnake-server/)

#### [2018 Tutorial Slides](https://docs.google.com/presentation/d/1PU3PMb6J7AD91qkHQD24IcBFWMuLXXusvOgswfgYI3Q/edit?usp=sharing)

#### [2017 Info Session Slides](http://sendwithus.github.io/battlesnake/present/#/)

## Starter & Example Snakes

Starter Snakes provided by Sendwithus (Heroku Ready)

* [battlesnake-node](https://github.com/sendwithus/battlesnake-node)
* [battlesnake-python](https://github.com/sendwithus/battlesnake-python)
* [battlesnake-go](https://github.com/sendwithus/battlesnake-go)
* [battlesnake-ruby](https://github.com/sendwithus/battlesnake-ruby)
* [battlesnake-clojure](https://github.com/sendwithus/battlesnake-clojure)

Example Snakes provided by Giftbit

* [typescript snake](https://github.com/Giftbit/battlesnake-node-typescript)

Other Example Snakes

* [battlesnake-java](https://github.com/tflinz/BasicBattleSnake2018)
* [battlesnake-elixir](https://github.com/nbw/battlesnake-elixir)

Traitor Snake (Winner of Battlesnake 2016, Advanced Division)

* [github.com/noahspriggs/battlesnake-python](https://github.com/noahspriggs/battlesnake-python)

## Running Your Own Game Server (With Docker)

This list of steps will work on Mac OS X or on Linux, if you are on Windows please use the vagrant setup.

* [Install Docker](https://docs.docker.com/install/)
* Run `docker run -it --rm -p 3000:3000 sendwithus/battlesnake-server`
* Visit `http://localhost:3000` *NOTE:* Docker runs on a virtual lan so when you add a snake to the game you cannot use localhost, use your internal IP instead.

## Running Your Own Game Server (With Vagrant)

This list of steps will work on Windows/Mac OS X/Linux

* [Install Virtual Box](https://www.virtualbox.org/wiki/Downloads)
* [Install Vagrant](https://www.vagrantup.com/downloads.html)
* Create a directory somewhere on your computer
* Inside the created directory, create a file named Vagrantfile and save it with the following:

```vagrantfile
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "generic/alpine36"
  config.vm.network "forwarded_port", guest: 3000, host: 3000
  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.provider "virtualbox" do |vb|
    vb.name = 'Alpine1'
    vb.cpus = 1
    vb.memory = 1024
  end
  config.vm.provision "shell", inline: <<-SHELL
    echo http://dl-3.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories
    echo http://dl-3.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories
    apk update
    apk add docker
    rc-update add docker boot
    service docker start
    sleep 2
    docker run -td -p 3000:3000 sendwithus/battlesnake-server
  SHELL

end
```

* Open a terminal and cd into the created directory
* Run `vagrant up`
  * first time running this command with take a bit because of images that need to be downloaded
* Visit `http://localhost:3000` *NOTE:* The virtual machine runs on a virtual lan so when you add a snake to the game you cannot use localhost, use your internal IP instead.
* `vagrant halt` will stop the virtual machine, and `vagrant destroy` will remove it.

## Bounty Snakes

Bounty Snakes are snakes built by sponsoring teams. Teams that defeat a Bounty Snake will win its prize - some snakes have one big prize, others have prizes for all winners.

Bounty Snakes will be available at 3:00pm in the lobby. To challenge a Bounty Snake, visit the sponsor table in the lobby and tell them you'd like to challenge their Bounty. Challange Bounty Snakes from:

* GitHub
* Sendwithus
* Rooof
* Workday
* AppColony
* Redbrick
* Giftbit
* Checkfront
* Bambora
* Accio
* Semaphore

## FAQ

### Will there be food provided?

Yes, BattleSnake has partnered with four food trucks to provide lunch free of charge to all participants and volunteers. You will be given a lunch voucher to use when you check-in and register your team. The trucks will be located at the [Royal BC Museum](http://royalbcmuseum.bc.ca/visit/plan-your-visit/eat-drink).

### What should I bring for the day?

Bring your laptop with power adapter and a water bottle. That is it!

### Is there an after party this year

Yes, VIATEC is hosting the BattleSnake after party at Fort Tectoria! It will start right after the tournament is finished. Light appetizers and two complimentary drinks provided with entry (beer, wine, and non-alcoholic options).

### Can I work on my snake before the event

YES! We highly recommend it.

### How do I collect Bounty Snake prizes?

* If you want to collect a Bounty Snake prize you have to go to the company booth that is hosting that snake and challenge them to a duel. The company will run the battle and if your snake is victorious you will be awarded the prize. Each snake will have different win conditions so come prepared.

### When should I show up?

Check in and team registration will open at 8:30 am for folks attending the morning tutorial (9:00-10:00am). If you are not attending the tutorial, please arrive by 10:00am to check in and register your team. Orientation starts at 10:30am sharp.

## Community Resources

[Snakedown test server](https://play.snakedown.com/) created by Cory Binnersley to help you test your snake!

## Contributing

Have sample code you'd like to share? Have useful links? See a typo?

Create a Pull Request on Github or email us at [battlesnake@sendwithus.com](mailto:battlesnake@sendwithus.com).
=======
# battlesnake-python

A simple [BattleSnake AI](http://battlesnake.io) written in Python. 

Visit [battlesnake.io/readme](http://battlesnake.io/readme) for API documentation and instructions for running your AI.

This AI client uses the [bottle web framework](http://bottlepy.org/docs/dev/index.html) to serve requests and the [gunicorn web server](http://gunicorn.org/) for running bottle on Heroku. Dependencies are listed in [requirements.txt](requirements.txt).

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

#### You will need...

* a working Python 2.7 development environment ([getting started guide](http://hackercodex.com/guide/python-development-environment-on-mac-osx/))
* experience [deploying Python apps to Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
* [pip](https://pip.pypa.io/en/latest/installing.html) to install Python dependencies

## Running the Snake Locally

1) [Fork this repo](https://github.com/sendwithus/battlesnake-python/fork).

2) Clone repo to your development environment:
```
git clone git@github.com:username/battlesnake-python.git
```

3) Install dependencies using [pip](https://pip.pypa.io/en/latest/installing.html):
```
pip install -r requirements.txt
```

4) Run local server:
```
python app/main.py
```

5) Test client in your browser: [http://localhost:8080](http://localhost:8080).

## Deploying to Heroku

1) Create a new Heroku app:
```
heroku create [APP_NAME]
```

2) Deploy code to Heroku servers:
```
git push heroku master
```

3) Open Heroku app in browser:
```
heroku open
```
or visit [http://APP_NAME.herokuapp.com](http://APP_NAME.herokuapp.com).

4) View server logs with the `heroku logs` command:
```
heroku logs --tail
```

## Questions?

Email [battlesnake@sendwithus.com](mailto:battlesnake@sendwithus.com), or tweet [@send_with_us](http://twitter.com/send_with_us).
>>>>>>> 86ca17f94e866983409cb4c95c926e6069300e22
