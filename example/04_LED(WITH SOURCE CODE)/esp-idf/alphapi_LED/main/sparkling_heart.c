#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "alphapi.h"
void app_main(void)
{
    alphapi_display_init();
    char image_shower[2][6][6] = {\
        {".#.#.", \
         "#####", \
         "#####", \
         ".###.", \
         "..#.."},\
        {".....", \
         ".#.#.", \
         ".###.", \
         "..#..", \
         "....."}};
    while (1)
    {
        led_show_matrix(image_shower[0]);
        vTaskDelay(pdMS_TO_TICKS(500));
        led_show_matrix(image_shower[1]);
        vTaskDelay(pdMS_TO_TICKS(500));
    }
}