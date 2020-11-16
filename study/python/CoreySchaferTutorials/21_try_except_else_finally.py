#!/usr/bin/env python3

try:
    f = open('test')
    if f.name == 'corrupt_file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    # Else clause works when there's no Exception
    print(f.read())
    f.close()
finally:
    print("Executing Finally")
