int ledPin = 3;
int humanPin = 9;
int PWMValue = 0;

void setup() {
  Serial.begin(9600);
  pinMode(humanPin, OUTPUT);   
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int photoRegValue = analogRead(A0);
  PWMValue = map(photoRegValue, 0, 1023, 255, 0);
  Serial.print(PWMValue);

  bool humanDetected = false;

  // Read serial only if available
  if (Serial.available() > 0) {
    char human = Serial.read();
    humanDetected = (human == '1'); 
  }

  if (humanDetected) {
    digitalWrite(humanPin, HIGH);
    delay(500);
    if (photoRegValue < 200) {
      analogWrite(ledPin, 255);  // full ON
    } else {
      analogWrite(ledPin, PWMValue); // dim
    }

  } else {
    digitalWrite(humanPin, LOW);
    delay(500);
    if (photoRegValue > 900) {
      analogWrite(ledPin, 0);  // OFF
    } else {
      analogWrite(ledPin, PWMValue); // dim
    }
    
  }
}