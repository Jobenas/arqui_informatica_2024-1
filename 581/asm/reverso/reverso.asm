section .data
    mensaje db "Hola mundo", 0

section .bss
    inverse resb 20


section .text
    global _start

_start:
    mov rax, mensaje
    mov rbx, 0

_countLoop:
    inc rax
    inc rbx
    mov cl, [rax]
    cmp cl, 0
    jne _countLoop

    mov r8, rbx     ; almaceno el contador en registor r8
    mov r9, inverse
    mov rax, mensaje
    add rax, r8

_reverse:
    dec rax
    mov r10, [rax]  ; muevo de mensaje a inverse
    mov [r9], r10
    inc r9
    cmp rax, mensaje    ; comparo rax si ya llego a la direccion de mensaje
    jne _reverse

    mov [r9], byte 10   ; agrego enter
    inc rbx

    ; syscall para imprimir en terminal
    mov rax, 1
    mov rdi, 1
    mov rsi, inverse
    mov rdx, rbx
    syscall


    ; salgo del programa
    mov rax, 60
    mov rdi, 0
    syscall
