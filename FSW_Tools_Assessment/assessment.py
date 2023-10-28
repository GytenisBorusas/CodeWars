import os
import time
from mock_database import DatabaseHelper

def connect_to_database(D):
    D.connect_to_database("gzxw001.sierradatabase", "telemetry_db_17", "space_user", "space_secret_password")

def export_all_telemetry_items_as_csv(filename: str):
    """ Exports all telemetry items to a csv, 1 CSV per packet. """
    d = DatabaseHelper()
    connect_to_database(d)
    telemetry_packets = d.get_packets()

    for idx in range(0, len(telemetry_packets)):
        packet = telemetry_packets[idx]
        telemetryItems = d.get_telemetry_items()
        telemetryPacketItems = d.get_packet_telemetry_items()
        enumeration_items = d.get_telemetry_enums()
        enumeration_values = d.get_telemetry_enum_values()

        # current_time = time.time()

        # headers
        with open(filename + "_" + packet.name + ".csv", "w+") as file:
            file.write("Telemetry Item ID, Name, Parent Name, Data Type, Telemetry Item Number, Packet Item Number, Enumeration Name\n")

        # items
        for telemetry_item in telemetryItems:
            telemetry_items_in_packet = [item for item in telemetryPacketItems if item.packet_id == packet.id and item.telemetry_item_id == telemetry_item.id]
            if telemetry_items_in_packet:
                # current_time = time.time()
                for t in telemetry_items_in_packet:
                    with open(filename + "_" + packet.name + ".csv", "a") as file:
                        enumeration = next((e.name for e in enumeration_items if e.id == telemetry_item.enumeration_id), None)
                        if telemetry_item.parent_id:
                            parent = [i for i in telemetryItems if i.id == telemetry_item.parent_id ][0]
                            file.write(f"{telemetry_item.id}, {telemetry_item.name},{parent.name}, {telemetry_item.datatype}, {telemetry_item.item_number}, {t.item_number}, {enumeration}\n")
                        elif not telemetry_item.parent_id:
                            file.write(f"{telemetry_item.id}, {telemetry_item.name},,{telemetry_item.datatype}, {telemetry_item.item_number}, {t.item_number}, {enumeration}\n")

if __name__ == "__main__":
    print("Running export...")
    start_time = time.time()
    export_all_telemetry_items_as_csv(os.path.expanduser("~/Downloads/telemetry-items"))
    end_time = time.time()
    print("Finished.")
    print(f"Export took {end_time-start_time:0.2f} seconds to run")

