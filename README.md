# LLVM2

## About

* This is a Python version of (LLVM1)[https://github.com/sokoide/llvm1]

## How to run

* Run
```sh
pip install -r requirements
python main.py
```

* builtin.c defines `write` and `writeln` funcitons and compiled into builtin.ll

```sh
$ clang -emit-llvm -S -O -o builtin.ll /path/to/builtin.c
```

* link them into linked.ll

```sh
$ llvm-link out.ll builtin.ll -S -o linked.ll
```

* run with the interpreter

```sh
$ lli linked.ll
42
$ echo $?
42
```

* compile it into a native binary

```sh
$ llc linked.ll -o linked.s
$ clang linked.s -o linked
$ ./linked
42
$ echo $?
42
```


