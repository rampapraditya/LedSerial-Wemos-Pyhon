import serial
import serial.tools.list_ports
import time

def detect_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        # Memeriksa deskripsi atau nama port
        if "Arduino" in port.description or "CH340" in port.description or "USB-SERIAL" in port.description:
            return port.device
    return None

def led_on():
    arduino.write(b'1')
    print("LED Menyala")

def led_off():
    arduino.write(b'0')
    print("LED Mati")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Mencoba mendeteksi dan menghubungkan ke Arduino/Wemos
    arduino_port = detect_arduino_port()

    if arduino_port:
        print(f"Arduino ditemukan di port {arduino_port}")
        # Inisialisasi koneksi serial ke Arduino/Wemos
        arduino = serial.Serial(arduino_port, 9600)
        time.sleep(1)  # Tunggu Arduino siap

        kondisi = True

        try:
            while kondisi:
                # Membaca input dari pengguna
                print("1 untuk menyalakan LED, 0 untuk mematikan LED, 2 untuk menghentikan program.")
                command = input("input : ")

                # Kirim perintah ke Arduino jika input adalah 1 atau 0
                if command == '1':
                    arduino.write(b'1')
                    print("Mengirim perintah: LED Menyala")
                elif command == '0':
                    arduino.write(b'0')
                    print("Mengirim perintah: LED Mati")
                elif command == '2':
                    kondisi = False
                    print("Program dihentikan")

                else:
                    print("Perintah tidak valid. Masukkan 1 atau 0.")

        except KeyboardInterrupt:
            print("Program dihentikan")
        finally:
            arduino.close()

    else:
        print("Arduino/Wemos tidak terdeteksi di port mana pun.")