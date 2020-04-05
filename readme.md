

Description
===========

kfuzz is a simple fuzzer as suggested in the exercise and does roughly the same thing: Based on a word
list or via brute force it executes a binary with an argument and collects the output. In the event of a
program crash, the parameters of the execution are displayed to inform the user of possible vulnerabilities
in the program. It can use a list of arguments stored in a text file or generate arguments for format string
and buffer overflow attacks. The lists in the resources directory are taken from OWASP, which has a wiki
article providing common fuzz vectors. The program is best tried out with those files for a quick proof of
concept. The format string input generator generates all possible combinations of format string inputs with
replacement up to a certain length - this might take forever. The program is written in Python3 and will
probably not work with an older interpreter.

Usage
=====

Flags
-----

The program allows certain flags to be passed in order to change its behavior:
-target 

:	The program to be executed.

-vectors 

:	Path to file with arguments.

-fstring 

:	Run with format string brute force generator (max. length = 16337).

-oflow 

:	Run with input strings consisting of ’A’s (max. length = 16337).

-threads 

:	Set number of threads. Default = 20.

Example calls
-------------


``` {#lst:orgcode language="c" caption="Original code" label="lst:orgcode"}
kfuzz.py −target resources/test_programs/format
 −vectors ./resources/attack_vector_lists/format_string_vectors.txt
kfuzz.py −target resources/test_programs/format
 −vectors ./resources/attack_vector_lists/buffer_overflow_vectors.txt
kfuzz.py −target ../resources/test_programs/canary −oflow
kfuzz.py −target ../resources/test_programs/canary −fstring
```
