#include <stdio.h>
#include "bmp.h"

int main(){
    // Image Filename
	char filename[] = "input.bmp";
    Bmp bmp;

    // Open bmp image
    if (openBMP(&bmp, filename)){
        int width = getWidth(&bmp);
        int height = getHeight(&bmp);

        unsigned char r, g, b;
        for( int y=height-1; y>=0; y--){
            for( int x=0; x<width; x++ ){
                // Obtain the rgb value of a pixel at (x, y)
                getPixelData(&bmp, x, y, &r, &g, &b);

            }
        }

        // Release bmp memory
        freeBmp(&bmp);
    }
    else{
        printf("Fail to open bmp file");
        return 0;
    }
    return 0;
}
