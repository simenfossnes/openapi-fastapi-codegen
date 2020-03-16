# OpenAPI Spec -> FastAPI | CodeGen

<p align="center">
  <a href="#"><img src=".github/illustration.svg" /></a>
</p>

Generate FastAPI server stubs based on an open api specification file.


## TODOs

- [x] add illustration.
- [x] make this list.
- [ ] extend and vectorize cases (may use numpy cases for this. ? )
- [x] make tail-recursion on the interpreter, allowing "flatter" parsing. ?  - resolved using inheritance.
- [ ] Add command line execution and configs 
- [ ] add requirements.txt + requirements in README
- [x] Add string formatting / fix automation so that the naming has a max-length and no whitespace
- [x] fix references and inheritance using these "allOf" etc. 
- [ ] implement proper documentation of methods in interpretaiton-class. 
- [ ] callable generation of OAS via CLI 
- [x] resolve whether to import from DataModel or generate schemas in the OAS-app. - No need to. 
- [x] also resolve whether then to import selectively (track required external imports) - no need

Note on imports: all resolved via yaml-reading with relative imports. 