#include<LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);

void setup(){
    lcd.init();
    lcd.clear();
    lcd.backlight();
    // lcd.setCursor(2,0);
    // lcd.print("Hello Nayan!");
    // delay(1000);
    Serial.begin(9600);
}
void loop(){
    if (Serial.available() > 0){
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.print(Serial.readStringUntil("\n"));
    }
}