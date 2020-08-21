auto-decider
============

auto-decider is a small python script for generating BDSM tasks, inspired by Reddit's r/FapDeciders.

## Installation

To install auto-decider, simply clone this repository to a location of your choice.

## Usage

To generate a task, execute decider.py

Previous to doing so, you may want to adjust the lists of toys at your disposal as well as likes and limits in config.json. 
The initial version of config.json will contain all categories currently used in "likes" as well as all toys used in "toys" and all anatomic parts distinguished in "anatomy".

## Contributing

The easiest way to contribute is adding more tasks to the tasks folder. Any .json file in this folder will be parsed on executing decider.py, so the file name can be used to describe the source.

Better refining the category list, both adding to or adjusting the ones available (listed in schema/definitions.json) and adjusting, which are used to categorize already existing tasks is also very welcome.
