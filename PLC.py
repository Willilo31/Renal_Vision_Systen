from pycomm3 import LogixDriver

# Configura la dirección IP del Micro820
plc_ip = "172.17.0.1"  # Reemplaza con la dirección IP de tu Micro820

# Crea una instancia del controlador Logix
with LogixDriver(plc_ip) as plc:

    plc.write_tag('O:2/0', 1)

    # Espera un momento (puedes ajustar según sea necesario)
    plc.delay(1)

    # Apaga la salida
    plc.write_tag('O:2/0', 0)

