#include<LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);

void setup(){
    lcd.init();
    lcd.clear();
    lcd.backlight();
    lcd.setCursor(2,0);
    // lcd.print("Hello Nayan!");
    // delay(1000);
    Serial.begin(9600);
}
void loop(){
    if (Serial.available() > 0){

        lcd.clear();
        String data = Serial.readStringUntil("\n");

        int newlineindex = data.indexOf("\n");
        if(newlineindex != -1){
          String line1 = data.substring(0,newlineindex);
          String line2 = data.substring(newlineindex + 1);
          lcd.clear();

          lcd.setCursor(0,0);
          lcd.print(line1);
    
          lcd.setCursor(0,1);
          lcd.print(line2);
        }
    }
}