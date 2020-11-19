# Building Enterprise JavaScript Applications

Li, Daniel.
Building Enterprise JavaScript Applications: Learn to build and deploy robust JavaScript applications using Cucumber, Mocha, Jenkins, Docker, and Kubernetes.
Packt Publishing. Kindle Edition.

## Chapter 3. Managing Version History with Git

Version Control System (VCS)

- Source Code Control System (SCCS, released in 1972)
- Revision Control System (RCS, released in 1982)
- Concurrent Versions System (CVS, released in 1990)
- Apache Subversion (SVN, released in 2000)
- Git (released in 2005)

### Setting up Git

#### Configuring Git

We can configure Git using the `git config` command. This command will manipulate the `.git/config` file on our behalf.

- Local: Applies only to the current repository. The configuration file is stored at `<repository-root>/.git/config`
- Global: Applies to all repositories under the user's home directory. The configuration file is stored at `$HOME/.config/git/config` and/or at `$HOME/.gitconfig`, with the latter being only available in newer versions of Git. `$HOME/.gitconfig` will override `$HOME/.config/git/config`
- System: Applies to all repositories in your machine. The configuration file stored at `/etc/gitconfig`

#### Configuring a user

```bash
git config --global user.name "Daniel Li"
git config --global user.email "dan@danyll.com"
```

### Learning the basics

#### Understanding file states in Git

In Git, every file can be in one of two generic states: **tracked** and **untracked**.
The **tracked** state can be further subdivided into three substates: **modified**, **staged**, and **committed**.

Initially, all files exists in the **workspace** (also known as **working tree** or **working directory**) and are in the **untracked** state.

`git add` places the *untracked or modified file* into what is known as the **staging area**, which is also known as the **index** or **cache**. When a file is placed into the staging area, it is in the **staged state**.

- Workspace/working directory: All the files and directories currently in our filesystem
- Index/staging area/cache: All the modifications you want to commit
- Repository (the `.git` directory): Hosts a history of all your committed and tracked files

### Branching and Merging

#### Branching models

![Vincent Driessen's branching model](../assets/git-model@2x.png)

- Vincent Driessen, [A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)
- [Git Flow](https://github.com/nvie/gitflow)

##### The Driessen Model

In Driessen's model, there are two permanent branches:

- `develop`(or `dev`, or development): The main branch that developers work on.
- `master`: Only production-ready code can be committed to this branch. Here, production-ready means the code has been tested and approved by the stakeholders.

There are also other non-permanent branches:

- Feature branches: Branching from the `dev` branch, feature branches are used for developing new features, or fixing non-critical bugs. Feature branches will eventually be merged back into the `dev` branch.
- Release branches: Once enough features or bug fixes have been implemented and merged into the `dev` branch, a release branch can be created from the `dev` branch to undergo more scrutiny before being released. For instance, the application can be deployed onto a staging server to be UI and manually tested. Any bugs uncovered during this process would then be fixed and committed directly to the release branch. Once the release branch is **free** of bugs, it can then be merged into the `master` branch and released into production. *These fixes should also be merged back into the `dev` branch and any other release branches.*
- Hotfix (or patch) branches: Hotfixes are issues (not always bugs) that are in production which must be fixed as soon as possible, before the next planned release. In these cases, the developer would create a branch from `master`, make the required changes, and merge directly back into master. *These hotfix branches should also be merged back into the `dev` branch and any other release branches.*

##### Naming sub-branches

There are multiple valid ways to name these sub-branches, but the most popular convention uses grouping tokens, with various delimiters.

##### Using merge and rebase together

`git rebase` makes the history look cleaner and more linear, but loses the context of when and where changes are integrated together. So, I'd advise using `git rebase` for *feature/bug-fix* branches.

When integrating changes from a feature branch into the `dev` branch, or from the `dev` branch into `master`, use `git merge` because it provides context as to where and when those features were added. Furthermore, we should add a `--no-ff` flag to `git merge`, *which ensures the merge will always create a new commit, even when fast-forwarding is possible.*

### Releasing code

The release branch should be named after the version of the release, prefixed by `release/`, such as `release/0.1.0`. The code to be released should then be deployed to a staging server, where automated UI testing, manual testing, and acceptance testing should be conducted (more on these later).

#### Semantic versioning

In semver(Semantic versioning), everything is versioned with three digits, MAJOR.MINOR.PATCH, which start at 0.1.0 and are incremented as follows:

- Patch: After a backward-compatible hotfix
- Minor: After a backward-compatible set of features/bug fixes have been implemented
- Major: After a backward-incompatible change

#### Tagging releases

Tags, in Git, are markers that highlight certain points in the commit history as being important.

There are two types of tags:

- Lightweight tags: A pointer to a particular commit
- Annotated tags: Full objects in the Git database, similar to a commit. Annotated tags contain information about the tagger, the date, and an optional message.

We should use annotated tags to tag releases. Check out the master branch and add an annotated tag by running `git tag` with the `-a` flag. The name of the tag should be the semver version, and you should also add a message describing the release:

```bash
git checkout master
git tag -a 0.1.0 -m "Implement social login. Update user schema."
git show 0.1.0
```

### Hotfixes

Working on a hotfix branch is very similar to working on a release branch; the only difference is that we are branching off `master` instead of `dev`.

Adding a hotfix makes the Git history more complicated than before, and so hotfixes should only be made when absolutely necessary.
