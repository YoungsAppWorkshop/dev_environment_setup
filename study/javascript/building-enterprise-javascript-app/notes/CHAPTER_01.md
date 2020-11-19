# Building Enterprise JavaScript Applications

Li, Daniel.
Building Enterprise JavaScript Applications: Learn to build and deploy robust JavaScript applications using Cucumber, Mocha, Jenkins, Docker, and Kubernetes.
Packt Publishing. Kindle Edition.

## Chapter 1. The Importance of Good Code

The best way to improve process is

- Technical level: Test-Driven Development
- Management level: Agile principles, Scrum Framework

### Technical Debt

#### What is technical debt

Technical debt is a metaphor created by Ward Cunningham, an American computer programmer: "A little debt speeds development so long as it is paid back promptly with a rewrite... The danger occurs when the debt is not repaid. Every minute spent on not-quite-right code counts as interest on that debt."

##### Causes of technical debt

- Lack of talent
- Lack of time
- Lack of morale

##### Consequences of technical debt

- Development speed will slow down
- More manpower (and thus money) and time will need to be spent to implement the same set of features
- More bugs, which consequently means poorer user experience, and more personnel required for customer service

#### Repaying technical debt through refactoring

Clean means:

- Well-structured
- Well-documented
- Concise
- Well-formatted and readable

##### Defining processes

Good code starts with good planning, design, and management, and is maintained by good processes.

- Guidelines:
  - Situations where incurring technical debt is appropriate,
  - Time to repay technical debts
  - A rotation system like greenfield/brownfield projects within the team
  - **The Definition of Done**: Code passes all tests and is peer-reviewed, documentation is updated.

### Test-Driven Development

Test-Driven Development is a development practice created by Kent Beck, it requires the developer to write tests for a feature before that feature is implemented.

- It allows you to validate that your code works as intended.
- It avoids errors in your test suite, if you write your test first, then run it, and it does not fail, that's a prompt for you to check your test again.
- Since existing features would be covered by existing tests, it allows a test runner to notify you when a previously functional piece of code is broken by the new code(in other words, to detecting regressions).

#### Understanding the TDD process

TDD consists of a rapid repetition of the following steps:

- Identify the smallest functional unit of your feature that has not yet been implemented.
- Identify a test case and write a test for it.
- Run the test and see it fail.
- Write the minimum amount of code to make it pass.
- Refactor the code.

##### Fixing Bugs

In TDD, when a bug is encountered, it is treated the same way as a new feature — you'd first write a (failing) test to reproduce the bug, and then update the code until the test passes. Having the bug documented as a test case ensures the bug stays fixed in the future, preventing regression.

#### Benefits of TDD

For many developers, having tests in the code is an afterthought — a luxury if time permits. But what they don't realize is that everyone tests their code, consciously or otherwise.

Benefits of TDD includes:

- Avoiding manual tests
- Tests as specification
- Tests as documentation
- Short development cycles

##### Avoiding manual tests

You should formally define these manual tests as code, in the form of *unit, integration and end-to-end (E2E) tests*, among others. Formally defining tests has a higher initial cost, but the benefit is that the tests can now be automated.

Mike Cohn developed the concept of **the Testing Pyramid**, which shows that an application should have a lot of unit tests (as they are fast and cheap to run), fewer integration tests, and even fewer UI tests, which take the most amount of time and are the most expensive to define and run.

Needless to say, manual testing should only be done after unit, integration, and UI tests have been thoroughly defined.

##### Tests as specification

TDD forces you to think about your requirements and break them down into atomic units. TDD also helps you to abide by the You Aren't Gonna Need It (YAGNI) principle. Lastly, writing the tests (and thus the specifications) forces you to think about the interface that consumers of your function would have to use to interact with your function.

##### Tests as documentation

In fact, tests are the most comprehensive set of code samples there are, covering every use case that the application cares about.

##### Short development cycles

Because TDD focuses on a single functional block at a time, its development cycles are usually very short (minutes to hours). This means small, incremental changes can be made and released rapidly.

#### Difficulties with TDD adoption

- Inexperienced team
- Slower initial development speed
- Legacy code
- Slow tests

#### When not to use TDD

- When the project is a Proof-of-Concept (PoC)
- When the product owner has not defined clear requirements (or does not want to), or the requirements change every day.
