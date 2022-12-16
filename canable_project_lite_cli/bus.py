from can import Bus

from canable_project_lite_cli.com_port.connection_mode import auto_port_scan

lada_ph2_bus = Bus(
    bustype='slcan',
    channel=auto_port_scan(),
    bitrate=500000)
