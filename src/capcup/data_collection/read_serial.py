import serial

port = "COM5"
baud = 9600
logfile = "serial_log.txt"

with serial.Serial(port, baud, timeout=1) as ser, open(logfile, "w") as f:
    print(f"Logging from {port} to {logfile}")
    while True:
        try:
            line = ser.readline().decode(errors="ignore").strip()
            print(line)
            f.write(line + "\n")
            f.flush()
        except KeyboardInterrupt:
            print("\nStopped by user.")
            break
