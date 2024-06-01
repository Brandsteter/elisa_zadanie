import psycopg2
import json

def store_interface(cur, config_data, interface_type):
  interfaces = config_data["frinx-uniconfig-topology:configuration"]["Cisco-IOS-XE-native:native"]["interface"][interface_type]

  sql_query = """
  INSERT INTO interface (name, description, config, port_channel_id, max_frame_size) 
  VALUES (%s, %s, %s, %s, %s)
  """

  for interface in interfaces:
    name = interface_type + str(interface["name"])
    description = interface.get("description", None)
    config = json.dumps(interface)
    port_channel = interface.get("Cisco-IOS-XE-ethernet:channel-group", None)
    port_channel_id = None
    mtu = interface.get("mtu", None)

    if port_channel != None and port_channel["mode"] == "active":
      port_channel_id = get_portchannel_id(cur, port_channel["number"])

    data = (name, description, config, port_channel_id, mtu)
    cur.execute(sql_query, data)
  
  return True


def get_portchannel_id(cur, portchannel_number):
  sql_query = """
  SELECT id FROM interface WHERE name = %s
  """

  portchannel_name = "Port-channel" + str(portchannel_number)
  cur.execute(sql_query, (portchannel_name,))
  row = cur.fetchone()
  
  if row:
    return row[0]
  else:
    return None
