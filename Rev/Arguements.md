# Arguements



**Author** - MarshmalloQi

**Points** - 100

### Files provided:
- `my_gf.exe` A file with no extenion, probably an executable.
- [mail]() A link to a very familiar song /s.

### Analysing the files

We must first determine what type of a file `my_gf` is. For this, we use the `file` command on the terminal.

``` bash
$ file my_gf
my_gf: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=5dc7847161bfdb9b76f326a1dde651a8c6d47a8d, for GNU/Linux 4.4.0, not stripped

```

Hence it is an `ELF` executable file which we can run directly from the terminal. At first we need to change its permissions to allow execution using the `chmod` command and then execute it.

```
$ chmod +x my_gf
./my_gf

```
Output:
```text
This won't give you the flag!
```

So the file is now successfully being executed but it looks like it needs some appropriate arguement, as the name of the challenge suggests, to get the desired output. For this we need to analyse the internal structure of the `ELF` file using the right tool.

It is nearly impossible to obtain the original hand written code from a compiled program, but there are tools which sort of 'predict' what the program *should* look like in its code form.

These tools are called *decompilers* and one such decompiler is called **Ghidra**. We can either download ghidra sofware from the [official Github repo](https://github.com/NationalSecurityAgency/ghidra/releases) and use the editor or instead use the [dogbolt.org](dogbolt.org) website to use Ghidra and/or other decompilers at the same time.

In the output provided by Ghidra, we can find two functions of interest i.e. `main`:

```c
undefined8 main(int param_1)

{
  printf("This won\'t give you the flag!");
  if (5 < param_1) {
    printf("okay, you may have the flag, kiddo\nBut Remember\x1bc");
    source_func();
    printf("\n\n\n\n\n\n\nDon\'t be a script kiddie ");
  }
  return 0;
}
```

and `source_func`:

```c
void source_func(void)

{
  char cVar1;
  undefined *puVar2;
  size_t sVar3;
  int local_2c;
  
  local_2c = 0;
  while( true ) {
    sVar3 = strlen(flag_enc);
    puVar2 = key;
    if (sVar3 <= (ulong)(long)local_2c) break;
    cVar1 = flag_enc[local_2c];
    sVar3 = strlen(key);
    putchar((int)(char)puVar2[(ulong)(long)local_2c % sVar3] - 0x46U ^ (int)cVar1);
    local_2c = local_2c + 1;
  }
  return;
}
```

Here the main function checks for a condition and when it is true, it calls `source_func` to output the flag. While the `source_func` function contains the algorithm to decode the flag character-wise and then outputs it. Hence we need to find the *encoded flag* and then translate the *decoding mechanism*.

In my case, for some reason Ghidra software showed the full `key` as`xor_is_love` but an incomplete `flag_enc` as `{mob@XmCv]zZ[MFPYpJEokZ@_FTDuJvR`. So I needed to find the complete flag by directly looking into the file. We can do this by either opening the file as text using a hex editor like **010 Editor** or by simply using the string command on the terminal as:

```bash
strings my_gf
```
Output:
```text
/lib64/ld-linux-x86-64.so.2
putchar
strlen
__libc_start_main
__cxa_finalize
printf
libc.so.6
GLIBC_2.34
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
PTE1
u3UH
AUATSH
[A\A]]
{mob@XmCv]zZ[MFPYpJEokZ@_FTDuJvRzmHsoF_`yE_qUvJuBJFRFo}@\X|EBkELom[NDm^
xor_is_love
This won't give you the flag!
okay, you may have the flag, kiddo
But Remember
Don't be a script kiddie 
;*3$"
...
```

This gives us the encoded flag as ``{mob@XmCv]zZ[MFPYpJEokZ@_FTDuJvRzmHsoF_`yE_qUvJuBJFRFo}@\X|EBkELom[NDm^`` and `xor_is_love` as the key.

Now on observing the `source_func` function, we can analyse that it uses a local variable `local_2c` as a count and uses it to take each character of `flag_enc` while cycling through `key` by taking modulus with its length to evaluate the new character using an expression.

## Solution Walkthrough

There are two possible solutions to this problem:
### Solution 1

**Step One** - Run the Ghidra software, create a project and upload the file `my_gf`.

**Step Two** - FInd the variables ``flag-enc="{mob@XmCv]zZ[MFPYpJEokZ@_FTDuJvRzmHsoF_`yE_qUvJuBJFRFo}@\X|EBkELom[NDm^"`` and `key="xor_is_love"` which are the encoded flag and the key required to decode it respectively.

**Step Three** - Translate the decoding mechanism in `source_func` using python or any other language which looks like:

```python
flag_enc=""
key=""
output = ""
count=0;
while count<len(flag_enc):
    output=output+(chr((ord(key[count%len(key)])-70)^ord(flag_enc[count])))
    count=count+1
print(output)
```

**Step Four** - Plug in the values of `flag_enc` and `key` and run the program to get the flag as output:
```
IDC{cute_mehra_still_this_will_be_a_very_long_flag_to_bruteforce_right}
```

### Solution 2

**Step One** - Open the terminal and head to the directory where the file exists.

**Step Two** - Execute the file providing 5 or more random arguements to reveal the flag.

```bash
$ chmod +x my_gf
$ ./my_gf arg1 arg2 arg3 arg4 arg5
```
Output:
```text
IDC{cute_mehra_still_this_will_be_a_very_long_flag_to_bruteforce_right}






Don't be a script kiddie
```

### Final flag : 
`IDC{cute_mehra_still_this_will_be_a_very_long_flag_to_bruteforce_right}`

## Key Concepts

- Using a decompiler to predict the behaviour of a compiled program.