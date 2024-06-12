section .data
    num db 0, 0
    numLen equ $ - num

section .text
    global _start

_start:
    mov ecx, 2
    mov eax, 3
    add ecx, eax        ; aca tengo 5 entero
    add ecx, 48         ; 48 es codigo ASCII para '0'
    mov eax, num
    mov [eax], ecx
    add eax, 1
    mov ecx, 10         ; codigo ASCII para \n
    mov [eax], ecx

    mov edx, numLen
    mov ecx, num
    mov ebx, 1
    mov eax, 4          ; Syscall (sys_write)
    int 0x80

    mov eax, 1          ; Syscall (sys_exit)
    int 0x80