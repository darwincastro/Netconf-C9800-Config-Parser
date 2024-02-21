from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom

router = {
   'host': '1.1.1.1',
   'port': '830',
   'username': 'admin',
   'password': 'admin'
}


m = manager.connect(host=router['host'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxe'}, hostkey_verify=False)

running_config = m.get_config('running').xml

# Parse the XML and pretty print it
pretty_xml = xml.dom.minidom.parseString(running_config).toprettyxml()

# Specify the file name where you want to save the output
output_file_path = 'local_path/c9800_running_config.xml'

# Open the file in write mode and write the XML content
with open(output_file_path, 'w') as output_file:
    output_file.write(pretty_xml)

# Print a message indicating the file has been created
print(f"XML content has been saved to {output_file_path}")

m.close_session()