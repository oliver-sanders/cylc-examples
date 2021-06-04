Managing Conda Environments
===========================

> **Note:** Requires Cylc>=8.0b1

Cylc does not (presently) provide any functionality for building or managing
the environments that your jobs use e.g:

* Conda environments.
* Python virtual environments.
* Docker/Singularity images.
* etc.

Cylc leaves you to handle builds and environments yourself.

This is a quick example showing how Conda environments can be built and used to
run jobs on different platforms.

* Environments are build on each platform

  > **Note:** If your platforms run the same operating system and share the
  > same architecture then you could use conda-pack to avoid building the
  > same environment in multiple places.
* Jobs are run using the `conda run` command.
* You must configure the path to your `conda.sh` script in the `flow.cylc` file

> **Note:** By fiddling the `CONDA_PREFIX` you could locate the Conda
> environments inside the Cylc run directory which means they would be
> removed by `cylc clean`.
