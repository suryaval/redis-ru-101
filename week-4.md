# week-4

## Bit Data

### BitField

  > Bitfield mykey set u8 0 42

  > Bitfield mykey get u8 0

  > Bitfield mykey incrby u8 1

       `43`

  > Type mykey

      ` "raw" `

```
Type:
	Signed(i)
	Unsigned(u)
Limits:
	i64
	U63
```

### BitArray

>	GETBIT key offset

>	SETBIT key offset value

>	BITCOUNT key [start end]

	BITCOUNT returns the count of the number of set bits only.
	BITCOUNT uses a zero based byte offset from the left of the string.
	
>	BITOP operation destkey key [key …]

	Allowed operations: AND OR XOR NOT

>	BITPOS key bit [start end]

	BITPOS can be used to find the index of the first set or unset bit.
	hscan "event:PDMM-JUOT-FPFF-BBLO" 0 match available:*
