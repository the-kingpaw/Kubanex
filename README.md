# Kubanex

Kubanex is an online forum application designed specifically for students. It provides a platform for students to collaborate, share knowledge, and discuss various topics related to their studies. The aim of Kubanex is to create a supportive and inclusive community for students to engage with one another, where they can share their thoughts and ideas, ask for help, and connect with like-minded individuals.

## Goals

- [ ] Collaborative discussion forums for students
- [ ] Ability to post questions and receive answers from peers
- [ ] Ability to connect with other students with similar interests
- [ ] Robust search functionality to easily find relevant discussions
- [ ] Notifications to keep you informed of new activity in the forums

## Getting Started

To get started with Kubanex, simply sign up for an account. Once you have created your account, you can start participating in discussions, asking questions, and connecting with other students.

## Contributing

We welcome contributions to Kubanex! If you have an idea for a new feature or have found a bug, please submit an issue on our GitHub repository. If you would like to contribute code, please fork the repository and submit a pull request.

To setup environment you have to clone this repository, and install requirement from `requirements.txt` like

```$ pip intall -r requirements.txt```

### Branching Strategy

`master` Branch: This is the main branch that contains the stable version of the codebase. Releases should be made from this branch.

`release` Branches: These are branches that are created from the development branch when you want to prepare a release. They are used to stabilize the code before it is merged into the master branch.

`development` Branch: This is the branch where all new features and bug fixes are developed. It is usually created from the master branch and is used to integrate the work of multiple developers.

`feature_` Branches: These are branches that are created from the development branch to work on a specific feature. They should be short-lived, meaning they should be deleted once the feature is completed and merged into the development branch.

`hotfix_` Branches: These are branches that are created from the master branch when you need to fix a critical bug in the stable codebase. They should be merged back into the master and development branches once the bug is fixed.

## License

BSD 3-Clause License

Copyright (c) 2023, Nikita Syrman, Inal Khutov, Sergey Vetrov

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.