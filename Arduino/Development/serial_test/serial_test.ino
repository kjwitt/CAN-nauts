// Pin 13 has an LED connected on most Arduino boards.
int ledState = LOW;   
int led = 13;
int comin=0;
int sensorPin = A0;    // select the input pin for the potentiometer
int sensorValue = 0;  // variable to store the value coming from the sensor
long previousMillis = 0; 
long interval = 1000;  
// the setup routine runs once when you press reset:
void setup() {           
// initialize the digital pin as an output.
pinMode(led, OUTPUT);  
Serial.begin(9600); //This initialices the USB as a serial port
}
// the loop routine runs over and over again forever:
void loop() {
  char incomingByte = (char)Serial.read();
  if(incomingByte=='1')
    digitalWrite(led,HIGH);
  else if(incomingByte=='0')
    digitalWrite(led,LOW);
}
  

