# Docker notes

Hanzhe Liang · 11 November 2026

[Lesson 08](https://khanlab.bio/cbio7501-f26/pages/08-containers.html), sections 1–4.
Docker Desktop 4.99.0, Docker Engine 29.9.3, Apple Silicon Mac.

## Run a container

```bash
docker --version
docker run --rm hello-world
docker run --rm ubuntu:24.04 cat /etc/os-release
docker run --rm ubuntu:24.04 bash -c "samtools --version || echo 'no samtools in plain Ubuntu'"
docker run --rm -it ubuntu:24.04 bash
# Inside the container:
ls /
exit
```

`hello-world` worked. The Ubuntu container reported version 24.04.5 LTS.
It could not find samtools, even though samtools is installed in the project's
Pixi environment on the Mac. The container has its own filesystem and tools.
The interactive Bash session also worked. `--rm` removed each container after
it exited; the downloaded images stayed available.

## Read the project files

From the project folder:

```bash
docker run --rm -v "$PWD":/work -w /work ubuntu:24.04 ls metadata
docker run --rm -v "$PWD":/work -w /work ubuntu:24.04 head -2 metadata/samples.tsv
```

The mount maps this project folder to `/work` inside the container. Quoting
`$PWD` matters because the local path contains spaces. The sample-table header
and first row matched the host output exactly when checked with `cmp`.

## Record the image

```bash
docker images
docker image inspect ubuntu:24.04 --format '{{.Id}}'
docker image inspect ubuntu:24.04 --format '{{index .RepoDigests 0}}'
```

The image ID returned by this installation was:

```text
sha256:fe81560990fae86dc4743202b2cb4d3df98d0bcf949173cecef15ce1127ef852
```

The repository digest was:

```text
ubuntu@sha256:fe81560990fae86dc4743202b2cb4d3df98d0bcf949173cecef15ce1127ef852
```

The tag `24.04` can point to an updated image later. The digest identifies the
downloaded content. Running by this digest also reported Ubuntu 24.04.5 LTS:

```bash
docker run --rm ubuntu@sha256:fe81560990fae86dc4743202b2cb4d3df98d0bcf949173cecef15ce1127ef852 cat /etc/os-release
```

The engine ran Linux arm64 containers. `docker ps -a` was empty at the end.
The LTEE image build starts in section 5 and is still to do.
