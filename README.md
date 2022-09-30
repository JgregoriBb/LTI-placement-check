
# LTI placement check for Blackboard Learn Ultra

This script checks LTI placements in Blackboard Learn Ultra corses and generates a report on their avaiability alongside other basic information such as title or creation date. As it may take some time to run, the script provides a progress bar for monitoring.

>:warning: NOT tested for Windows computers

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

3.Install dependencies, either from 'requirements.txt' or manually.

```Python
#dependencies from requeriments.txt
pip3 -r requeriments.txt

#dependencies manually
pip3 install Bb-rest-helper
pip3 install alive-progress
````

5.In the developer portal, register a new application and retrieve the KEY and SECRET values. Configure this application in Learn with an user with sufficient priviledges to

    * read course information
    * read course content

>:warning: Do NOT use an admin user to register your application!

More information can be found in Anthology´s [developer 
documentation page](https://docs.anthology.com/rest-apis/learn/getting-started/registry)

4.Within root, create a folder called "credentials" inside of that folder, create a file named "learn_config.json" and fill it with the following template with the KEY and SECRET values.

```json
{
    "url":"Learn Server url",
    "key":"KEY from dev portal",
    "secret":"SECRET from dev portal"
}
```

## Usage

Once setup is complete, the script can be run from a terminal.
1.Open a terminal and navegate to the root directory
2.Run the script with Python3

```Python
Python3 app.py
```

## Script results

The script generates a csv file named **lti_report.csv** with the following fields.

```csv
course_id,external_id,course_name,LTI_title,LTI_created,LTI_modified,LTI_available
```

## known issues

1.As logging is set to off for production if some errors appear those may be sent to the terminal. This is related to the Bb-rest-library and will be corrected in future versions of that library.

2.If you are interested in having detailed logs from the script uncomment lines 26 and 27 in the file **script-helper.py**. Again, a more elegant solution for this will be provided soon.

3.Testing for this development has been minimal feel free to open issues in this repository if you encounter problems or have enhancement suggestions.

