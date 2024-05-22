section .data
    msg db "Hola mundo!", 0xa ; String que deseo imprimir
    len equ $ - msg ; generar la longitud del string

section .txt
    global _start

_start: 
    mov edx, len
    mov ecx, msg
    mov ebx, 1
    mov eax, 4  ; system call (sys_write)
    int 0x80   

    mov eax, 1  ; systemcall (sys_exit)
    int 0x80