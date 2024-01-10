#include <Adafruit_NeoPixel.h>

#define PIN            6   // Define the pin where the data line is connected
#define NUMPIXELS      522 // Number of LEDs in the strip

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin();           // Initialize the strip
  strip.show();            // Initialize all pixels to 'off'
  strip.setBrightness(10); // Set brightness to 10% (max 255, so 10% of 255 is about 25)
//  Serial.begin(9600);
//  Serial.println("setup done...");
}

void loop() {
//  cube_animation();
  flower_animation();
}

void clear_LEDs(){
  for(int i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, strip.Color(0, 0, 0)); // Set color to 'off'
  }
}

int cube_outline[] = {148, 149, 150, 151, 152, 153, 154,
                      177, 171, 170,
                      184, 190, 192,
                      213, 207, 204,
                      220, 226, 230,
                      249, 243, 239,
                      256, 262, 266,
                      285, 279, 275,
                      292, 298, 302,
                      321, 315, 311,
                      328, 329, 330, 331, 332, 333, 334, 338,
                      356, 350, 347,
                      366, 372, 374,
                      390, 384, 383,
                      404, 405, 406, 407, 408, 409, 410};
                      
  int cube_fill[] = {176, 175, 174, 173, 172,
                   185, 186, 187, 188, 189, 191,
                   212, 211, 210, 209, 208, 206, 205,
                   221, 222, 223, 224, 225, 227, 228, 229,
                   248, 247, 246, 245, 244, 242, 241, 240,
                   257, 258, 259, 260, 261, 263, 264, 265,
                   284, 283, 282, 281, 280, 278, 277, 276,
                   293, 294, 295, 296, 297, 299, 300, 301,
                   320, 319, 318, 317, 316, 314, 313, 312,
                   335, 336, 337,
                   355, 354, 353, 352, 351, 349, 348,
                   367, 368, 369, 370, 371, 373,
                   389, 388, 387, 386, 385};
                   
void draw_cube(int outline_red, int outline_green, int outline_blue,
               int fill_red, int fill_green, int fill_blue){
  //  draw cube outline  
  for(int i = 0; i < sizeof(cube_outline) / sizeof(cube_outline[0]); i++) {
    int ledIndex = cube_outline[i];
    if (ledIndex < NUMPIXELS) {
      strip.setPixelColor(ledIndex, strip.Color(outline_red, outline_green, outline_blue));
    }
  }
  
  //  draw cube fill
  for(int i = 0; i < sizeof(cube_fill) / sizeof(cube_fill[0]); i++) {
    int ledIndex = cube_fill[i];
    if (ledIndex < NUMPIXELS) {
      strip.setPixelColor(cube_fill[i], strip.Color(fill_red, fill_green, fill_blue));
    }
  }
  strip.show();
}
                   
void cube_animation(){
  clear_LEDs();
  draw_cube(239, 0, 255, // outline - pink
          17, 0, 255); // fill - blue
  delay(200);
  
  clear_LEDs();
  draw_cube(77, 255, 0, // outline - neon green
          255, 137, 0); // fill - orange
  delay(200);

  clear_LEDs();
  draw_cube(119, 0, 255, // outline - purple
          255, 255, 0); // fill - yellow
  delay(200);
}

int flower_orange[] = {3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 41, 42, 43, 44, 45, 46, 47, 48, 49, 61, 62, 63, 64, 65, 66, 67, 80, 81, 82};
int flower_yellow[] = {316, 332, 333, 334, 352};
int flower_blue[] = {241, 242, 246, 247, 257, 260, 262, 265, 276, 280, 284, 294, 297, 300, 312, 313, 314, 318, 330, 331, 335, 338, 347, 351, 356, 364, 369, 374, 383, 387, 389, 393, 400, 403, 404, 406, 407, 410, 420, 421, 422, 426, 427, 428, 439, 443, 458, 462, 475, 479, 495, 497, 513};
int flower_green[] = {100, 117, 136, 153, 172, 189, 208, 225, 244, 261};

void draw_flower(){
  // draw orange
  for(int i = 0; i < sizeof(flower_orange) / sizeof(flower_orange[0]); i++) {
    strip.setPixelColor(flower_orange[i], strip.Color(255, 128, 0));
  }
  
  // draw yellow
  for(int i = 0; i < sizeof(flower_yellow) / sizeof(flower_yellow[0]); i++) {
    strip.setPixelColor(flower_yellow[i], strip.Color(255, 255, 0));
  }

  // draw blue
  for(int i = 0; i < sizeof(flower_blue) / sizeof(flower_blue[0]); i++) {
    strip.setPixelColor(flower_blue[i], strip.Color(0, 0, 255));
  }

  // draw green
  for(int i = 0; i < sizeof(flower_green) / sizeof(flower_green[0]); i++) {
    strip.setPixelColor(flower_green[i], strip.Color(0, 255, 0));
  }
  
  strip.show();
}

void flower_animation(){
  clear_LEDs();
  draw_flower();
  delay(5000);
}
