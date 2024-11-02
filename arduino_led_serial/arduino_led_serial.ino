const int ledPin = D13;

void setup() {
  // Atur pin LED sebagai output
  pinMode(ledPin, OUTPUT);

  // Memulai komunikasi serial dengan baud rate 9600
  Serial.begin(9600);
  Serial.println("Ketik '1' untuk menyalakan LED dan '0' untuk mematikan LED");
}

void loop() {
  // Cek apakah ada data yang masuk dari Serial
  if (Serial.available() > 0) {
    // Baca karakter dari Serial
    char command = Serial.read();
    
    // Cek jika command adalah '1' untuk menyalakan LED
    if (command == '1') {
      digitalWrite(ledPin, HIGH); // LED menyala
      Serial.println("LED Menyala");
    }
    
    // Cek jika command adalah '0' untuk mematikan LED
    else if (command == '0') {
      digitalWrite(ledPin, LOW); // LED mati
      Serial.println("LED Mati");
    }
  }

}
