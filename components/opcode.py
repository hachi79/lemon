import typing as t

__all__ = ("Opcode",)


class Opcode:
    __slots__ = ("inst",)
    """
    inst = hex(type|x|y|n|nn|nnn)
    format spec:
    type: (first nibble) the type operation
    x: (second nibble) general purpose register lookup
    y: (third nibble) general purpose register lookup
    n : (fourth nibble) 4-bit numeric value
    nn/kk: (third and fourth nibble) 8-bit immediate
    nnn: (second, third and fourth nibble) 12-bit immediate memory address
    """

    def __new__(cls, inst: int) -> t.Self:
        if isinstance(inst, int) and len(str(inst)) < 6:
            self = super(Opcode, cls).__new__(cls)
            return self

        else:
            raise ValueError(f"BAD OPCODE: {inst}")

    def __init__(self, inst: int) -> None:
        self.inst = inst

    @property
    def type(self) -> int:
        value = self.inst & 0xF000
        return value

    @property
    def x(self) -> int:
        value = (self.inst & 0x0F00) >> 8
        return value

    @property
    def y(self) -> int:
        value = (self.inst & 0x00F0) >> 4
        return value

    @property
    def n(self) -> int:
        value = self.inst & 0x000F
        return value

    @property
    def kk(self) -> int:
        value = self.inst & 0x00FF
        return value

    @property
    def nnn(self) -> int:
        value = self.inst & 0x0FFF
        return value

    def __repr__(self) -> str:
        return f"Opcode(inst={hex(self.inst)})"
