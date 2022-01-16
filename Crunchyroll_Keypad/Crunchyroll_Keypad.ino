void setup() {

  // Pins that will read the inputs the user provide through the buttons
  pinMode(2, INPUT);
  pinMode(4, INPUT);
  pinMode(6, INPUT);
  pinMode(8, INPUT);
  pinMode(10, INPUT);

  Serial.begin(9600); // Serial initialization
}

void loop() {
  
  // Storing the states (on and off) of each button in a variable
  // If any button is pressed, then write a signal that can be read for the python script, so it can execute tasks in Crunchyroll

  int switch1State = digitalRead(2);
  if (switch1State == LOW){digitalWrite(7, LOW);}
  else {digitalWrite(7, HIGH);Serial.println("Launching the app"); delay(1000);}

  
  int switch2State = digitalRead(4);
  if (switch2State == LOW){digitalWrite(7, LOW);}
  else {digitalWrite(7, HIGH);Serial.println("Previous Chapter"); delay(1000);}
  
  
  int switch3State = digitalRead(6);
  if (switch3State == LOW){digitalWrite(7, LOW);}
  else {digitalWrite(7, HIGH);Serial.println("Next Chapter"); delay(1000);}

  
  int switch4State = digitalRead(8);
  if (switch4State == LOW){digitalWrite(7, LOW);}
  else {digitalWrite(7, HIGH);Serial.println("Saving Chapter and Exit"); delay(1000);}
  
  int switch5State = digitalRead(10);
  if (switch5State == LOW){digitalWrite(7, LOW);}
  else {digitalWrite(7, HIGH);Serial.println("Instructions"); delay(1000);}
  
}
