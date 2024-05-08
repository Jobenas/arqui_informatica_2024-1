section .data
    userMsg db "Por favor ingrese un numero: "
    lenUserMsg equ $-userMsg
    dispMsg db "Ha ingresado: "
    lenDispMsg equ $-dispMsg
    new_line db 10

section .bss
    num resb 5


section .text
    global _start

_start:
    mov edx, lenUserMsg
    mov ecx, userMsg
    mov ebx, 1
    mov eax, 4      ; sys_write
    int 0x80

    mov edx, 5
    mov ecx, num
    mov ebx, 2
    mov eax, 3      ; sys_read
    int 0x80

    mov edx, lenDispMsg
    mov ecx, dispMsg
    mov ebx, 1
    mov eax, 4      ; sys_write
    int 0x80

    mov edx, 5
    mov ecx, num
    mov ebx, 1
    mov eax, 4      ; sys_write
    int 0x80

    mov eax, 1
    int 0x80
