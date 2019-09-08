int i = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Teensy Counting Sketch");
  
}

void loop() {
  // put your main code here, to run repeatedly:

  i++;
  Serial.println(i);
  delay(1000);
}
