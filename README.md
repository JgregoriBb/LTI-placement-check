# Bb_rest_helper_template
Template repository for projects based on the Bb-rest-helper library


# Project name

Project description

## Setup

This script was created in Python 3, make sure Python3 is installed and working in your system. Here are the steps to make it work.

1. Download or clone the repository.
2. Create a virtual environment and activate it.
```Python
#env creation
python3 -m venv env

#env activation
source env/bin/activate
```
3. Install dependencies, either from 'requirements.txt' or manually.
```Python
#dependencies from requeriments.txt
pip3 -r requeriments.txt

#dependencies manually
pip3 install Bb-rest-helper
pip3 install jupyter
````
5. In the developer portal, register a new application and retrieve the KEY and SECRET values. Configure this application in Learn with an user with sufficient priviledges to 
    
    * list required priviledges
    * list required priviledges
    * list required priviledges

>:warning: Do NOT use an admin user to register your application!

>:warning: Make sure to log a ticket to raise the API rate

More information can be found in Anthology´s [developer 
documentation page](https://docs.anthology.com/rest-apis/learn/getting-started/registry)

4. Within root, create a folder called "credentials" inside of that folder, create a file named "learn.config.json" and fill it with the following template with the KEY and SECRET values.
```json
{
    "url":"Learn Server url",
    "key":"KEY from dev portal",
    "secret":"SECRET from dev portal"
}
```
## Usage

Once setup is complete, the script can be run from a terminal.
1. Open a terminal and navegate to the root directory
2. Run the script with Python3
```Python
Python3 app.py
```
## Script results

