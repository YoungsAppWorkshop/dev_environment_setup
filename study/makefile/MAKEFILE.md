# Makefile Tutorial

## Structure

```bash
# Comments
# VARIABLE = value
FC = gfortran
# <target>: <dependency>
#    <command> # Tab
stats.exe: stats.o stats_func.o
    $(FC) -o stats.exe stats_func.o stats.o
```

## Examples

```make
.EXPORT_ALL_VARIABLES:
FLASK_APP=flaskr
FLASK_ENV=development

debug:
	flask run

init:
	flask init-db
```

**More Read**:

- [GNU Make Docs](https://www.gnu.org/software/make/manual/make.html)
- Stack Overflow: [How to set child process' environment variable in Makefile](https://stackoverflow.com/questions/23843106/how-to-set-child-process-environment-variable-in-makefile/23845391#23845391)
