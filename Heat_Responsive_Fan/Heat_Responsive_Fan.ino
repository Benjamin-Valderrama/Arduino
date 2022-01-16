const int sensorPin = A0;
const float baselineTemp = 23.0;

void setup() {
  Serial.begin(9600);

  pinMode(9, OUTPUT);
  digitalWrite(9, LOW);
  
}

void loop() {
  
  int sensorVal = analogRead(sensorPin);

  //Serial.print("Sensor Value : ");
  //Serial.print(sensorVal);

  float voltage = (sensorVal/1024.0) * 5.0;

  //Serial.print(", Volts : ");
  //Serial.print(voltage);

  float temperature = (voltage - .5) * 100;
  Serial.print("Degrees C :");
  Serial.println(temperature);


  if(temperature < baselineTemp){
    digitalWrite(9, LOW);
    } else {
      digitalWrite(9,HIGH);
    } 

  delay(1000);

}
