- Garden irrigation system with life weather update
- Garden defense system against cats. Work in progress.

The system consists of a rasperry pi (with wlan module), a arduino, a webcam. The arduino opens and closes relays. I use the ones from tinkerkit (see: http://store.arduino.cc/product/T010010). The relays steers the 24V connected to 4 magnetic valves, where I connected water hoses. I use valve #3 as the main valve, directly at the faucet, so that the water hoses are not constantly under pressure. 
The arduino is connected serially by USB to the raspberry pi. The serial protocol is as simple as possible:
o[valveNr] opens a valve and
c[valveNr] closes the valve.
In order to not flood my garden, the arduino will switch off automatically a opened valve after 30 seconds. It will do this independently for each valve.
On the raspberry pi run several python daemons. In order to try out to open and close the valve, one can use the simple ov.py module:

import ov
from time import sleep
ov.o(3)
sleep(15)
ov.c(3)

The main daemon is irrigationClient.py. It reads weather information from the database (I use an account at exosite for storing weather information and other stuff. At a later point, I will use a local db, e.g. mongodb). Depending on the temperature in the last 6 hours, it will open the valves at different times for a temperature depending amount of time. Currently, I use ov.py to open and close valves from irrigiationClient.py . At a later point, I want to use a rpc server (rpcServer.py), where a client connects to. This will help to integrate a web app (work in progress...), where the valves can also be controlled through a node.js interface. 
weather.py reads local weather data from openWeatherMap.org and store it in the db. Add your location in config.json.
The system is configured by a json string in config.json.

IN the cats directory you find a very early prototype of my cat defense system. 


