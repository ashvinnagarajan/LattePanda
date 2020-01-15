long lastTime = 0;

const int voltagePin = A5;
const float VOLTAGE_CALIB = 0.969;

const int numReadings = 30;
float readings[numReadings];      // the readings from the analog input
int index = 0;                  // the index of the current reading
float total = 0;                  // the running total
float average = 0;                // the average

float current = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(voltagePin, INPUT);
  for (int thisReading = 0; thisReading < numReadings; thisReading  )
    readings[thisReading] = 0;
}

void loop()
{
  if (millis() - lastTime > 1000)
  {
    lastTime = millis(); 
    
    total = total - readings[index];
    readings[index] = analogRead(0); //Raw data reading
    //Data processing:510-raw data from analogRead when the input is 0;
    // 5-5v; the first 0.04-0.04V/A(sensitivity); the second 0.04-offset val;
    readings[index] = (readings[index]-512)*5/1024/0.04-0.04;

    total= total - readings[index];
    index = index + 1;
    if (index >= numReadings)
      index = 0;
    average = total/numReadings;   //Smoothing algorithm (http://www.arduino.cc/en/Tutorial/Smoothing)
    current = average;

    int voltage_raw = analogRead(voltagePin);
    float voltage = 5*VOLTAGE_CALIB*(voltage_raw/0.091)/1023;
    
    Serial.println(voltage);
    Serial.println(current);
  }
}
