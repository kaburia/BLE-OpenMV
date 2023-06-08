#include <ArduinoBLE.h>

void setup() {
  // Initialize Serial communication
  Serial.begin(921600);

  // Initialize BLE
  if (!BLE.begin()) {
    Serial.println("Failed to initialize BLE");
    while (1);
  }

  Serial.println("BLE initialized");
}


void loop() {
  // Scan for BLE devices
  BLE.scan();

  // Check if a specific device is found
  BLEDevice peripheral = BLE.available();

  if (peripheral) {
    // Connect to the device
    if (peripheral.address() == "00:11:22:33:44:55") { // Replace with the desired device address
      Serial.print("Connecting to device: ");
      Serial.println(peripheral.address());

      if (peripheral.connect()) {
        Serial.println("Connected to device");
      }
    }
  }
}
