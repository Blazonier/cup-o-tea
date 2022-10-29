@echo off

cd src

nasm -f elf32 boot.s -o boot.o
gcc -m32 -c kernel.c
elf-ld -Ttext 0x0 boot.o kernel.o -o boot.bin

cd ..

del bin\boot.bin

copy src\boot.bin bin\ 
del src\boot.bin
del src\kernel.o
del src\boot.o

cd bin 

qemu-system-x86_64 -kernel boot.bin

cd ..
