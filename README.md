 
# sign-up

## PTR-532

In order to be registered as a collaborator to this organization, you must complete *one* task detailed in the upcoming section. The tasks are allocated on a first-come first-serve basis, **one per user**.
(If there are no tasks left, you can take any task not assigned **by your team**).

## Steps

1. (If you don't have a GitHub account yet, create one using your email address and your full first and last name **in English**.- **you did**)
2. Create an [issue](https://github.com/ptr-05/sign-up/issues/new) detailing the desired task you wish to be assigned. Be sure to include a description of the task in your own words, to be sure that you understood what needs to be done. The first user to create an issue for a given task, will be given that tasks. If a user requests a previously allocated task, then will have to start the process over again.
3. Create a branch in this repository named `feature/my-task-name` *(using lower-kabob-case only)*, replace `my-task-name` with a short description of your task.
4. Complete the task based on its description on your branch in a sub-folder of the root of the project.
5. If you have any questions regarding the task, you can post a *comment* in the issue created during *step 2*. All comments and communication must be in English. Be sure to tag `@ptr5mentor` in your comment.
6. Once you are finished, create a [pull request](https://github.com/ptr-05/sign-up/compare) with your solution. Be sure to also link your *open issue* with the pull request *(using the `Closes #...`)*.
7. The task is considered complete once it was merged.
8. Good luck!

## Rules

- You are free to look at StackOverflow, GitHub, forums, documentation, etc. during the learning process. However, solutions cannot be copied from any of the abovementioned sources. **Solutions must be yours, and yours only!**
- You are to complete the assignment alone.
- You only need to provide the code used to solve the tasks and not the actual environment *(when relevant)*.

## Tasks

### 1. [FastAPI](https://fastapi.tiangolo.com/)

Deploy a simple `http` server with two endpoints:

1. An endpoint that appends a `json` payload to a local file.
2. An endpoint that returns the last 10 payloads from the persisted file.

### 2. [Typer](https://typer.tiangolo.com/)

Create a simple `cli` tool with two commands:

1. A command that appends a `json` argument to a local file.
2. A command that returns the last 10 arguments from the persisted file.

### 3. [VitePress](https://vitepress.dev/)

Deploy a simple VitePress instance with two pages:

1. A landing page containing information a *fake* software tool from your imagination.
2. An installation guide for the above mentioned tool.

### 4. Dockerfile

Create a Dockerfile using a base image of your choice that contains the following:

- The `ffmpeg` package.
- An entrypoint that will run the `ffmpeg` package.

### 6. Coordinate Conversion

Convert *decimal degrees (DD)* to *degrees minutes seconds (DMS)* in the language of your choosing. Example coordinated:

```json
{
  "anchorage":   {
    "dd":  [-149.9002, 61.2181, 22],
    "dms": [[149, 54, 0.72, "W"], [61, 13, 5.16, "N"], 22]
  },
  "los_angeles": {
    "dd":  [-118.2437, 34.0522],
    "dms": [[118, 14, 37.32, "W"], [34, 3, 7.92, "N"]]
  }
}
```

### 7. Convert Markdown

Programmatically convert a markdown document to a PDF in any language.

### 8. [Numpy](https://numpy.org/)

Given an image of choosing, create histogram of RGB colors found in the image using `numpy`.

### 9. Password Strength

Write a tool that when provided a password, it will return `true` if it passes the following criteria”:

1. Contains at least 1 lowercase character.
2. Contains at least 1 uppercase character.
3. Contains at least 1 special character.
4. Contains at least 1 digit.
5. Minimum length of 8 characters.
6. A character cannot be repeated more than twice.
7. No sequences of 3 consecutive characters *(i.e. `abc`, `xyz`, `123`)*.

