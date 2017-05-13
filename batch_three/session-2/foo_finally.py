#!/usr/bin/python3
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)


