long lastTime = 0;

const int voltagePin = A5;
const float VOLTAGE_CALIB = 0.969;

const int numReadings = 30;
float readings[numReadings];      // the readings from the analog input
int index = 0;                  // the index of the current reading
float total = 0;                  // the running total
float average = 0;                // the average

float currentValue = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(voltagePin, INPUT);
  for (int thisReading = 0; thisReading < numReadings; thisReading++)
    readings[thisReading] = 0;
}

void loop()
{
  if (millis() - lastTime > 1000)
  {
    lastTime = millis(); 
    currentValue = analogRead(A6);

    int voltage_raw = analogRead(voltagePin);
    float voltage = 5*VOLTAGE_CALIB*(voltage_raw/0.091)/1023;

    Serial.print("Cur: ");
    Serial.println(currentValue);
    Serial.print("Vlt: ");
    Serial.println(voltage);
  }
}
