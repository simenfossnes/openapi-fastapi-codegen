# OpenAPI Spec -> FastAPI | CodeGen

<p align="center">
  <a href="#"><img src=".github/illustration.svg" /></a>
</p>

Generate FastAPI server stubs based on an open api specification file.

<br>

## 🚀 Get Up and Running in 5 Minutes

You can get everything up and running in five minutes or less, following these steps:

1. **Install the CLI.**

   ```shell
   pip install ofc-cli
   ```

1. **Generate your first codebase**

   ```shell
   ofc spec.yaml -o ./spec 
   ```

<br>

## 📁 Folder Structure

The folder structure has been carefully architected. Each element is briefly described. 
Improvement suggestions are greatly appreciated.

    ├── routes/                 # incoming requests routed to handlers
    ├── handlers/               # logic handling incoming requests
    ├── models/                 # data models used in the project
    │
    ├── main.py                 # the main file of the project
    │
    ├── Dockerfile              # a list of commands defining the container image
    ├── .dockerignore           # files & folders to be ignored by docker
    ├── Pipfile                 # modern python dependency management
    ├── Pipfile.lock            # full & deterministic environment specification
    ├── .gitignore              # files & folders to be ignored by git

<br>

## 🛠️ What’s Included?

The tech stack has been carefully selected. All reasoning is found below each element. You are free to question why the tools has been chosen, and to suggest improvements.

- ⚡ **FastAPI** - _a modern, fast (high-performance), web framework for building APIs._
  <details>
  <summary>Reasoning</summary><br>
  
  We needed a web framework to support developer productivity and high execution performance in python.

  We checked out the [Techempower Web Framework Benchmarks for python](https://www.techempower.com/benchmarks/#section=data-r19&hw=cl&test=fortune&l=zijzen-1r) and
  saw a few high-performing web frameworks. Based on this, we manually reviewed the top performers from a developer experience perspecitve. We found that FastAPI was 
  the framework with the highest overall value to support developer productivity and execution performance.
  
  </details>

<br>

## 📝 ToDo

There's still a way to go. Contributions appreciated!

- [x] add illustration.
- [x] make this list.
- [ ] extend and vectorize cases (may use numpy cases for this. ? )
- [x] make tail-recursion on the interpreter, allowing "flatter" parsing. ?  - resolved using inheritance.
- [ ] Add command line execution and configs 
- [ ] add requirements.txt + requirements in README 
- [x] Add string formatting / fix automation so that the naming has a max-length and no whitespace
- [x] fix references and inheritance using these "allOf" etc. 
- [ ] implement proper documentation of methods in interpretaiton-class. 
- [ ] ❗ callable generation of OAS via CLI 
- [x] resolve whether to import from DataModel or generate schemas in the OAS-app. - No need to. 
- [x] also resolve whether then to import selectively (track required external imports) - no need
- [ ] Make script to build and resolve inherited types from DataModel-yaml. (seems resolution only goes so far)
- [ ] Make automated imports of utilized and extended models from the above datamodel (may be tricky)

Note on imports: all resolved via yaml-reading with relative imports. 
