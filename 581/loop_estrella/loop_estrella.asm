section .data
    cont db 9
    star db "*"
    new_line db 10

section .text
    global _start

_start:
    loop:
        mov edx, 1
        mov ecx, star
        mov ebx, 1
        mov eax, 4      ; system call (sys_write)
        int 0x80

        mov ebx, cont
        mov al, [ebx]
        sub al, 1
        mov [ebx], al
        cmp al, 0
        jne loop

    mov edx, 1
    mov ecx, new_line
    mov ebx, 1
    mov eax, 4      ; system call (sys_write)
    int 0x80

    mov eax, 1
    int 0x80        ; system call (sys_exit)