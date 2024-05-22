section .data
    msg db "Hola mundo!", 0xa       ; String del mensaje a mostrar
    len equ $ - msg

section .text
    global _start

_start:
    mov edx, len
    mov ecx, msg
    mov ebx, 1
    mov eax, 4      ; System call (sys_write)
    int 0x80        ; Generamos interrupcion para que ejecute el system call

    mov eax, 1      ; System call (sys_exit)
    int 0x80        ; Generamos interrupcion para que ejecute el system call