#include "bmp.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int openBMP(Bmp* bmp, char *fileName)
{
    FILE *file;
    if ( (file = fopen(fileName, "rb") ) == NULL ) {
        fprintf(stderr, "Error: bmpLoad(), File open fail!\n");
        return 0;
    }

    fread( (uint8_t*) &(bmp->header), 1, SIZE_OF_HEADER, file );

    // Check whether a bmp image file
    if( bmp->header.bfType != 0x4d42 ){
        fprintf(stderr, "This file is not .BMP!!\n");
        return 0;
    }

    // Read header of the bmp file
    fread( (uint8_t*) &(bmp->info), 1, SIZE_OF_INFO, file );

    printf("Image Informations:");
    printf("Image depth: %d\n", bmp->info.biBitCount);
    printf("Image size: %d\n", bmp->info.biSize);
    printf("Image width: %d\n", bmp->info.biWidth);
    printf("Image height: %d\n", bmp->info.biHeight);
    printf("Image compress: %d\n", bmp->info.biCompression);

    // Check if 24 bits color depth
    if ( bmp->info.biBitCount != 24 ){
        fprintf(stderr, "The file is not 24 bits!!\n");
        return 0;
    }

    // Revise the image width, because in the bmp format, the memory of width
    // direction would align at forth multiple in memory address.
    // 修正圖片的寬度為4的倍數，因為記憶體會以 4 bytes 方式對齊
    while( bmp->info.biWidth % 4 != 0 )
        bmp->info.biWidth++;

    int size = bmp->info.biWidth*sizeof(Pixel)*bmp->info.biHeight;
    bmp->data = (Pixel*)malloc(size);
    
    // Load pixel data
    fread( (uint8_t*)bmp->data, 1, size, file );
    fclose(file);

    return 1;
}

void getPixelData(Bmp* bmp, int x, int y, uint8_t* r, uint8_t* g, uint8_t* b){
    *r = bmp->data[(y * bmp->info.biWidth) + x].r;
    *g = bmp->data[(y * bmp->info.biWidth) + x].g;
    *b = bmp->data[(y * bmp->info.biWidth) + x].b;
}

int getWidth(Bmp* bmp){
    return bmp->info.biWidth;
}

int getHeight(Bmp* bmp){
    return bmp->info.biHeight;
}

void freeBmp(Bmp* bmp){
    free(bmp->data);
}
