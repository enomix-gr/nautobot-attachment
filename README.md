Nautobot plugin to support any kind of attachments in Nautobot objects

### Installation
- clone repo
- `cd nautobot-attachment`
- activate Nautobot's venv
- `pip install .`
- add `nautobot_attachment` in the PLUGINS section of your `nautobot_config.py`
- from your NAUTOBOT_ROOT `nautobot-server migrate nautobot_attachment`

### Comments
Currently only Locations are supported.  
Many thanks to the awesome [Nautobot](https://networktocode.com/nautobot/) team!
