redef class Sys
	var carry_bit = false
	var b3 = 0x00u8
end

redef class Byte
	fun rol: Byte do
		var nxt_c = (self & 0b1000_0000u8) != 0u8
		var tmp = self << 1
		if sys.carry_bit then tmp += 1u8
		sys.carry_bit = nxt_c
		return tmp
	end

	fun ror: Byte do
		var nxt_c = (self & 0b0000_0001u8) != 0u8
		var tmp = self >> 1
		if sys.carry_bit then tmp += (1u8 << 7)
		sys.carry_bit = nxt_c
		return tmp
	end

end

fun nesasm(instr: Text): Bytes do
	var hx1 = once "703053A1D3703F64B316E4045F3AEE42B1A137156E882AAB".hexdigest_to_bytes
	var hx2 = once "20AC7A25D79CC21D58D01325966ADC7E2EB4B410CB1DC266".hexdigest_to_bytes
	var outstr = new Bytes.empty

	var a = 0u8
	var x = 0u8
	var stack = new Array[Byte]
	sys.carry_bit = false
	sys.b3 = 0x00u8
	for i in [0 .. instr.bytes.length[ do
		a = instr.bytes[i]
		x = a
		a = a.rol
		a = x
		a = a.rol
		x = a
		a = a.rol
		a = x
		a = a.rol
		x = a
		a = a.rol
		a = x
		a = a.rol
		stack.push a
		a = sys.b3
		x = a
		a = a.ror
		a = x
		a = a.ror
		x = a
		a = a.ror
		a = x
		a = a.ror
		sys.b3 = a
		a = stack.pop
		sys.carry_bit = false
		a += sys.b3
		a ^= hx1[i]
		sys.b3 = a
		x = a
		a = a.rol
		a = x
		a = a.rol
		x = a
		a = a.rol
		a = x
		a = a.rol
		x = a
		a = a.rol
		a = x
		a = a.rol
		x = a
		a = a.rol
		a = x
		a = a.rol
		a ^= hx2[i]
		outstr[i] = a
		#print a
	end
	return outstr
end

var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "

var instr = new FlatBuffer.from("A" * 24)

for i in [0 .. 24[ do
	var outstr = nesasm(instr)
	var j = 0
	while outstr[i] != 0u8 do
		instr[i] = t[j]
		outstr = nesasm(instr)
		j += 1
	end
end

print instr
