from pyModbusTCP.client import ModbusClient
import csv

def funcion (ip, pt = 502, d_id = 1, save_csv = False , beginning = 0, ending= 10):
    client = ModbusClient(host = ip, port = pt, unit_id = d_id)
    available_registers = []
    for register in range(beginning, ending+1):
        available_registers.append(client.read_holding_registers(register))
    
    if save_csv:
        with open("exported_data.csv","w") as file:
            writer = csv.writer(delimiter=",", quotechar="", quoting=csv.QUOTE_MINIMAL)
            for row in available_registers:
                writer.writerow(row)
                print("Data exported")