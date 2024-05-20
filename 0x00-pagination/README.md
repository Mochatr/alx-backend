# Pagination API Project

## Introduction

This project involves the creation of a RESTful API that allows clients to paginate through datasets efficiently. By the end of this project, developers should be able to implement various pagination techniques including simple pagination with `page` and `page_size` parameters, pagination with hypermedia metadata (HATEOAS), and deletion-resilient pagination.

## Resources

**Read or Watch:**
- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)
- [use this data file](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240520%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240520T131331Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=64c58c1328b8fe079ead77c59f7a1b4b6ccc29bc9c2874cd87c7e314f89ae0f4)

## Learning Objectives

Upon completion of this project, you should be able to:
- Implement pagination using simple `page` and `page_size` parameters.
- Enhance pagination with hypermedia metadata (HATEOAS).
- Design deletion-resilient pagination strategies.

## Requirements

- All files must be run on Ubuntu 18.04 LTS using Python 3.7.
- Every file must end with a new line.
- The first line of all executable files should be `#!/usr/bin/env python3`.
- A mandatory `README.md` file at the root of the project folder.
- Code must adhere to the pycodestyle (version 2.5.*).
- File lengths will be tested using `wc`.
- All modules should have documentation accessible via `python3 -c 'print(__import__("my_module").__doc__)'`.
- All functions should have documentation accessible via `python3 -c 'print(__import__("my_module").my_function.__doc__)'`.
- Documentation must be a full sentence explaining the purpose of the module, class, or method.
- All functions and coroutines must be type-annotated.
