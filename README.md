# Netconf-C9800-Config-Parser

**Disclaimer:** This script is not officially endorsed or provided by Cisco Systems. It is created and maintained by me. Use of this script is at your own risk. The script is provided "as is" without warranty of any kind, either expressed or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose.

This Python script is designed to fetch the running configuration of a Cisco Catalyst 9800 wireless controller and save it as an XML file. It uses the ncclient library to connect to the device using the NETCONF protocol and retrieve the running configuration. The script then pretty-prints the configuration using the xml.dom.minidom library and writes the output to an XML file.

## Features
- **NETCONF Connection:** The script establishes a NETCONF connection to a Cisco Catalyst 9800 wireless controller.
- **Running Configuration Retrieval:** It retrieves the running configuration of the device.
- **XML Parsing and Pretty Printing:** The script parses the retrieved configuration, which is in XML format, and pretty-prints it for better readability.
- **XML File Writing:** It writes the pretty-printed XML content to a file.
  
## Usage
1. Update the router dictionary with the details of your device.
2. Run the script.
3. The script will connect to your device, retrieve the running configuration, pretty-print it, and write it to a file named c9800_running_config.xml in the specified local path.
4. You can then open this file to view the running configuration of your device.

## Dependencies
This script uses the following Python libraries:

- ncclient for NETCONF connection and configuration retrieval.
- pprint for pretty-printing Python data structures.
- xmltodict for parsing XML.
- xml.dom.minidom for pretty-printing XML.

To run this script, make sure you have these libraries installed in your Python environment. If not, you can install them using pip:
```
pip install ncclient pprint xmltodict
```

## Example

The script connects to a Cisco Catalyst 9800 wireless controller using NETCONF, retrieves its running configuration, pretty-prints it, and writes it to an XML file named c9800_running_config.xml. This allows you to easily view and analyze the running configuration of your device.

> Please remember to replace '1.1.1.1', '830', 'admin', 'admin' with your actual router's IP, NETCONF port, username, and password, respectively. Also, replace 'local_path' with your actual local path where you want to save the output XML file.
