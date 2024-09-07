#include <string.h>
#include "driver/uart.h"
#include "driver/gpio.h"

const uart_port_t alphapi_uart_display_write_num = UART_NUM_1;
uart_config_t uart_config = {
    .baud_rate = 460800,
    .data_bits = UART_DATA_8_BITS,
    .parity = UART_PARITY_DISABLE,
    .stop_bits = UART_STOP_BITS_1, 
    .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
    .rx_flow_ctrl_thresh = 122,
};
int calc_checksum(char *data)
{
    int sum = 0, data_len = strlen(data) - 1;
    for (int i = 0; i < data_len; ++ i)
        sum += data[i];
    return sum & 0xff;
}
bool uart_write(char addr, char *data)
{
    if (strlen(data) == 0)
        return false;
    char byteToWrite[101] = "";
    byteToWrite[0] = 0x90, byteToWrite[1] = addr, byteToWrite[2] = strlen(data);
    strcat(byteToWrite, data);
    strcat(byteToWrite, " ");
    byteToWrite[strlen(byteToWrite)] = 0;
    byteToWrite[strlen(byteToWrite) - 1] = calc_checksum(byteToWrite);
    for (int i = 1; i <= 3; ++ i)
        uart_write_bytes(alphapi_uart_display_write_num, byteToWrite, 9);
    return true;
}
void alphapi_display_init()
{
    ESP_ERROR_CHECK(uart_param_config(alphapi_uart_display_write_num, &uart_config));
    ESP_ERROR_CHECK(uart_set_pin(alphapi_uart_display_write_num, 8, 9, UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE));
    // Setup UART buffered IO with event queue
    const int uart_buffer_size = (1024 * 2);
    QueueHandle_t uart_queue;
    // Install UART driver using an event queue here
    ESP_ERROR_CHECK(uart_driver_install(alphapi_uart_display_write_num, uart_buffer_size, uart_buffer_size, 10, &uart_queue, 0));
    char alphapi_display_test[6] = {4, 4, 4, 4, 4};
    uart_write(0x08, alphapi_display_test);
}
void led_show_matrix(char show_image[6][6])
{
    bool to_row[6][6];
    char led_image_res[6] = {0, 0, 0, 0, 0};
    for (int i = 0; i < 5; ++ i)
        for (int j = 0; j < 5; ++ j)
        {
            if (show_image[i][j] == '.')
                to_row[j][i] = 0;
            else if (show_image[i][j] == '#')
                to_row[j][i] = 1;
            else
            {
                printf("The provided image format is incorrect\n");
                exit(1);
            }
        }
    for (int i = 0; i < 5; ++ i)
    {
        led_image_res[i] += to_row[i][4] * 0x08 + to_row[i][3] * 0x10 + to_row[i][2] * 0x20 + to_row[i][1] * 0x40 + to_row[i][0] * 0x80;
        if (led_image_res[i] == 0) led_image_res[i] = 0x04;
    }
    uart_write(0x08, led_image_res);
}