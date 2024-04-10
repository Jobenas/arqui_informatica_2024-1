

memory = [
    b"\x60",
    b"\x80",
    b"\xa0",
    b"\xc1",
    b"\xff",
]

PC = 0
IR = 0
A = 0


def load_instruction():
    global IR, PC
    IR = memory[PC]


def update_pc(inc: int):
    global PC
    PC += inc


def fetch():
    load_instruction()
    update_pc(1)


def decode():
    global IR
    opcode = int.from_bytes(IR, "little") & 0xe0
    match opcode:
        case 0x60:
            return "IN A"
        case 0x80:
            return "OUT A"
        case 0xa0:
            return "DEC A"
        case 0xc0:
            return "JNZ"
        case 0xe0:
            return "HALT"


def execute(inst: str):
    global A, IR, PC

    match inst:
        case "IN A":
            A = int(input("Ingrese un numero: "))
        case "OUT A":
            print(A)
        case "DEC A":
            A = A - 1
        case "JNZ":
            if A != 0:
                PC = int.from_bytes(IR, "little") & 0x0f
        case "HALT":
            exit()


if __name__ == '__main__':
    while True:
        fetch()
        instruction = decode()
        execute(instruction)
