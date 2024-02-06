from pyModbusTCP.client import ModbusClient
import csv

def registers_sweeper(ip, pt=502, d_id=1, save_csv=False, beginning=0, ending=10):
    """
    Collects data from Modbus registers and optionally exports it to a CSV file.

    Args:
        ip (str): The IP address of the Modbus server.
        pt (int, optional): The Modbus server's port (default is 502).
        d_id (int, optional): The Modbus device ID or unit ID (default is 1).
        save_csv (bool, optional): Whether to save the collected data to a CSV file (default is False).
        beginning (int, optional): The starting Modbus register address to read (default is 0).
        ending (int, optional): The ending Modbus register address to read (default is 10).

    Returns:
        None

    This function connects to a Modbus server, reads holding registers within the specified range, and
    optionally exports the data to a CSV file. If an error occurs during the data reading process, it
    will be printed, but any successfully collected data will be saved to the CSV file (if requested).

    Example usage:
    registers_sweeper("192.168.1.100", pt=502, d_id=1, save_csv=True, beginning=0, ending=10)
    """
    client = ModbusClient(host=ip, port=pt, unit_id=d_id)
    available_registers = {}

    try:
        for register in range(beginning, ending+1):
            value = client.read_holding_registers(register)
            if value is not None:
                available_registers[register] = value[0]
                print(f"register {register} value: {value}")

    except Exception as e:
        print(f"Error reading data: {e}")

    if save_csv:
        with open(f"exported_data_id_{d_id}.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Register", "Value"])
            for register, value in available_registers.items():
                writer.writerow([register, value])
            print("Data exported")
