#ifndef BMP_H
#define BMP_H

#include <stdint.h>

#define SIZE_OF_HEADER 14
#define SIZE_OF_INFO 40

/* Structure to store pixel data */
typedef struct _Pixel{
    uint8_t b;
    uint8_t g;
    uint8_t r;
}Pixel;

/* Structure to store header data */
typedef struct _BmpHeader {                 //(14 bytes)
    uint16_t bfType;                        //(2 bytes)         File type, in BMP case, it¡¦ll be ¡¥BM¡¦(0x424D)
    uint32_t bfSize;                        //(4 bytes)        BMP file size
    uint16_t bfReserved1;                   //(2 bytes)        Always 0
    uint16_t bfReserved2;                   //(2 bytes)        Always 0
    uint32_t bfOffbytes;                    //(4 bytes)        Size of Headers + Palette, 14 + 40 + 4 * 28 in our case
} BmpHeader; 
 
 /* Structure to store info data */
typedef struct _BmpInfo{                    //(40 bytes)
    uint32_t biSize;                        //(4 bytes)        After Windows 3.X, it¡¦s always 40, which is the structure size of BITMAPINFOHEADER
    int32_t biWidth;                        //(4 bytes)        The width of image
    int32_t biHeight;                       //(4 bytes)        The height of image
    uint16_t biPlanes;                      //(2 bytes)        How many images in this file. For BMP, it¡¦s  always 1
    uint16_t biBitCount;                    //(2 bytes)        How many bits stand for a pixel, 8 in our case
    uint32_t biCompression;                 //(4 bytes)        0 is no compression, 1 is 8-bitRLE compression, 2 is 4-bitRLE compression.
                                            //        We only deal with no compression image.
    uint32_t biSizeImage;                   //(4bytes)         The image size after compress. If no compression, it could be 0 or image size
    int32_t biXPelsPerMeter;                //(4bytes)        horizontal dots per meter
    int32_t biYPelsPerMeter;                //(4bytes)        vertical dots per meter 
    uint32_t biClrUsed;                     //(4bytes)        How many colors used in palette, 0 for all colors
    uint32_t biClrImportant;                //(4bytes)        How many colors are important, 0 for all
} BmpInfo; 

typedef struct _Bmp{
    BmpHeader header;
    BmpInfo info;
    Pixel* data;
}Bmp;

/* Open a bmp file with the filename
 * @Params:
 *  bmp: Pointer of `Bmp struct`
 *  filename: Char array, name of the image file
 * @Return:
 *  1: Succeed to read image
 *  0: Failed to read image
 */
int openBMP(Bmp* bmp, char *fileName);

/* Get width informaton */
int getWidth(Bmp* bmp);

/* Get height informaton */
int getHeight(Bmp* bmp);

/* Get specific pixel's rgb value with position (x, y) given */
void getPixelData(Bmp* bmp, int x, int y, uint8_t* r, uint8_t* g, uint8_t* b);

/* Release allocated memory */
void freeBmp(Bmp* bmp);

#endif
