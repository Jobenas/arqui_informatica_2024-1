section .data
    num db 0, 0

section .text
    global _start

_start:
    mov ecx, 2
    mov eax, 3
    add ecx, eax
    add ecx, 48
    mov eax, num
    mov [eax], ecx
    add eax, 1
    mov ecx, 10
    mov [eax], ecx

    mov edx, 2
    mov ebx, 1
    mov ecx, num
    mov eax, 4  ; system call (sys_write)
    int 0x80   

    mov eax, 1  ; systemcall (sys_exit)
    int 0x80