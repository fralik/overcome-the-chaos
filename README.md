# overcome-the-chaos

## Information about this fork

This is a very simple project to show diffirent build systems applied to
a python project with focus on machine learning. It is a fort of
[https://github.com/artofai/overcome-the-chaos](https://github.com/artofai/overcome-the-chaos).
Differences between build systems are highlighted in the [blog post](https://habr.com/en/post/451962/).

### Usage

One can find files for various build systems (and task schedulers) inside the project.
Here is the list of tested systems:

* [CMake](https://cmake.org/) configuration is in [CMakeLists.txt](https://github.com/fralik/overcome-the-chaos/blob/master/CMakeLists.txt).
* [Pynt](https://github.com/rags/pynt) configuration is in [build.py](https://github.com/fralik/overcome-the-chaos/blob/master/build.py).
* [Paver](https://github.com/paver/paver) configuration is in [pavement.py](https://github.com/fralik/overcome-the-chaos/blob/master/pavement.py).
* [pydoit](http://pydoit.org/) configuration is in [dodo.py](https://github.com/fralik/overcome-the-chaos/blob/master/dodo.py).
* [Luigi](https://github.com/spotify/luigi) configuration is in [luigitasks.py](https://github.com/fralik/overcome-the-chaos/blob/master/luigitasks.py).

I checked how these systems can do the following:

1. Allow user to describe tasks and dependencies between tasks.
2. Support incremental builds, i.e. build only targets that have been changed.
3. Support incremental builds if source code has been changed.
4. Keep track of all the artifacts created during the build process in order to delete them with `clean` command.

The results are summariezed in the table below.
```
+-----------------------------------+-------+------------+------+-------+
|                                   | CMake | Pynt/Paver | doit | Luigi |
+===================================+=======+============+======+=======+
| Targets with dependencies         | yes   | yes        | yes  | yes   |
| Incremental builds                | yes   | no         | yes  | no    |
| Incremental builds on code change | yes   | no         | yes  | no    |
| Auto-generated clean command      | yes   | no         | yes  | no    |
+-----------------------------------+-------+------------+------+-------+
```

# Original README below

## Disclaimer

This is a very simple sample project written to be an example for series
of my posts on medium. It does not do anyting cool but it pretends to ;)
The idea is to show how to prepare your ML project for production environment,
not to explore bleeding-edge algorithms ;) Please refer my blog:

1. [Structure and automated workflow for a machine learning project — part 1](https://towardsdatascience.com/structure-and-automated-workflow-for-a-machine-learning-project-2fa30d661c1e)
2. [Structure and automated workflow for a machine learning project — part 2](https://towardsdatascience.com/structure-and-automated-workflow-for-a-machine-learning-project-part-2-b5b420625102)

## Introduction

OTS is a project aimed to provide REST like API for classifying between various iris classes.

## Installing

TBD

## API

TBD
