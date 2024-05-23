<p>
    <img src="assets/images/hugebnb.png">
</p>

<h1 align="center">HugeBnB</h1>
<p align="center">An AirBnB clone</h1>

---

## Description :house:

HugeBnB is a complete web application, integrating database storage, a backend API, and a front-end interface.

The first part of the project is to develop a command line interface to manage my HugeBnB objects.

### Phase 1 
> #### Each tasks is linked and will help to:
>
> - Create a new object (ex: a new User or a new Place)
> - Retrieve an object from a file, a database etc…
> - Do operations on objects (count, compute stats, etc…)
> - Update attributes of an object
> - Destroy an object

#### Execution
The shell should work in interactive mode:
```
$ ./console.py
(hugeBnB) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hugeBnB) 
(hugeBnB) 
(hugeBnB) quit
```
But also in non-interactive mode:
```
$ echo "help" | ./console.py
(hugeBnB)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hugeBnB) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hugeBnB)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hugeBnB) 
$
```